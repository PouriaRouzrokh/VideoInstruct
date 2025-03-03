import os
import re
from typing import List, Optional, Dict, Tuple
import litellm

from videoinstruct.configs import DocEvaluatorConfig
from videoinstruct.prompt_loader import DOC_EVALUATOR_SYSTEM_PROMPT

class DocEvaluator:
    """Evaluates documentation quality using LLMs."""
    
    def __init__(self, config: Optional[DocEvaluatorConfig] = None) -> None:
        """Initialize the DocEvaluator with the given configuration."""
        self.config = config or DocEvaluatorConfig()
        self.model_provider = self.config.model_provider
        self.rejection_count = 0
        self.conversation_history = [{"role": "system", "content": self.config.system_instruction}]
        self.feedback_history: List[str] = []
        
        if self.config.api_key:
            providers = {
                "deepseek": "DEEPSEEK_API_KEY",
                "openai": "OPENAI_API_KEY",
                "anthropic": "ANTHROPIC_API_KEY"
            }
            if self.model_provider in providers:
                os.environ[providers[self.model_provider]] = self.config.api_key
    
    def evaluate_documentation(self, documentation: str) -> Tuple[bool, str]:
        """Evaluate the quality of the provided documentation."""
        if len(self.conversation_history) == 1:  # Only system message exists
            evaluation_prompt = f"""
            Please evaluate the following documentation for quality, clarity, and completeness:
            
            ```markdown
            {documentation}
            ```
            
            Provide your evaluation according to the criteria in your instructions.
            """
        else:
            evaluation_prompt = f"""
            I've revised the documentation based on your feedback. Please evaluate this updated version:
            
            ```markdown
            {documentation}
            ```
            
            Has it improved? Are there still issues that need to be addressed?
            """
        
        self.conversation_history.append({"role": "user", "content": evaluation_prompt})
        response = self._get_llm_response(self.conversation_history)
        self.conversation_history.append({"role": "assistant", "content": response})
        
        python_code_match = re.search(r'```python\s*({.*?})\s*```', response, re.DOTALL)
        
        if python_code_match:
            try:
                result = eval(python_code_match.group(1).strip())
                if isinstance(result, dict) and "approved" in result and "feedback" in result:
                    is_approved = bool(result["approved"])
                    feedback = str(result["feedback"])
                    
                    if not is_approved:
                        self.feedback_history.append(feedback)
                        self.rejection_count += 1
                    else:
                        self.rejection_count = 0
                    
                    return is_approved, feedback
            except Exception:
                pass
        
        # Fallback: Use heuristics
        is_approved = "approved" in response.lower() and not any(x in response.lower() for x in ["reject", "not approved", "disapproved"])
        
        feedback_match = re.search(r'feedback["\']:\s*["\'](.+?)["\']', response, re.DOTALL | re.IGNORECASE)
        feedback = feedback_match.group(1) if feedback_match else response
        
        if not is_approved:
            self.feedback_history.append(feedback)
            self.rejection_count += 1
        else:
            self.rejection_count = 0
        
        return is_approved, feedback
    
    def evaluate_documentation_with_pdf(self, documentation: str, pdf_path: str) -> Tuple[bool, str]:
        """Evaluate documentation with PDF (uses text-based evaluation for compatibility)."""
        return self.evaluate_documentation(documentation)
    
    def should_escalate_to_user(self) -> bool:
        """Determine if evaluation should be escalated to a human user."""
        return self.rejection_count >= self.config.max_rejection_count
    
    def reset_rejection_count(self) -> None:
        """Reset the rejection count."""
        self.rejection_count = 0
    
    def reset_memory(self) -> None:
        """Reset conversation history, feedback history, and rejection count."""
        self.conversation_history = [
            {"role": "system", "content": self.config.system_instruction}
        ]
        self.feedback_history = []
        self.rejection_count = 0
    
    def get_feedback_history(self) -> List[str]:
        """Get the history of feedback provided."""
        return self.feedback_history
    
    def get_conversation_history(self) -> List[Dict[str, str]]:
        """Get the full conversation history."""
        return self.conversation_history
    
    def _get_llm_response(self, messages: List[Dict[str, str]]) -> str:
        """Get a response from the LLM."""
        model_name = self.config.model
        if self.model_provider != "openai" and "/" not in model_name:
            model_name = f"{self.model_provider}/{model_name}"
        
        generate_config = {
            "drop_params": True
        }
        
        config_params = {
            "max_output_tokens": "max_tokens",
            "temperature": "temperature",
            "top_p": "top_p",
            "stream": "stream",
            "seed": "seed"
        }
        
        for param, config_key in config_params.items():
            if getattr(self.config, param, None) is not None:
                generate_config[config_key] = getattr(self.config, param)
        
        if model_name == "anthropic/claude-3-7-sonnet-latest":
            generate_config["thinking"] = {"type": "enabled", "budget_tokens": 1024}
            generate_config["temperature"] = 1
        
        try:
            response = litellm.completion(
                model=model_name,
                messages=messages,
                **generate_config
            )
            return response.choices[0].message.content
        except Exception as e:
            try:
                return response.choices[0].message.reasoning_content
            except:
                return f"Error: {str(e)}"