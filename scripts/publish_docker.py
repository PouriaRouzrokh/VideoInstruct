#!/usr/bin/env python3
"""
Build and publish the VideoInstruct Docker image to Docker Hub.

Usage:
    python publish_docker.py [--version VERSION] [--no-push] [--repository REPO]

Example:
    python publish_docker.py --version 1.0.0
    python publish_docker.py --repository yourusername/videoinstruct
"""

import os
import sys
import getpass
import argparse
import subprocess
from pathlib import Path

# Configuration
DEFAULT_DOCKER_REPO = "videoinstruct/videoinstruct"
DEFAULT_VERSION = "latest"

def run_command(cmd: list, check: bool = True, input_str: str = None) -> bool:
    """Run a command and return its success status."""
    try:
        result = subprocess.run(
            cmd,
            check=check,
            capture_output=True,
            text=True,
            input=input_str
        )
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running command {' '.join(cmd)}: {e}", file=sys.stderr)
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr, file=sys.stderr)
        return False

def check_docker_login() -> bool:
    """Check if user is logged in to Docker Hub and handle login if needed."""
    try:
        # Try to inspect Docker config file
        config_path = os.path.expanduser("~/.docker/config.json")
        if os.path.exists(config_path):
            print("Already logged in to Docker Hub")
            return True
            
    except Exception:
        pass
        
    print("You are not logged in to Docker Hub.")
    
    # Ask if user wants to login now
    response = input("Would you like to login now? [y/N]: ").lower()
    if response != 'y':
        print("Login required to push images to Docker Hub. Aborting.")
        return False
    
    # Get credentials
    username = input("Docker Hub username: ")
    password = getpass.getpass("Docker Hub password: ")
    
    # Try to login
    try:
        result = subprocess.run(
            ["docker", "login", "-u", username],
            input=password,
            text=True,
            capture_output=True,
            check=True
        )
        if "Login Succeeded" in result.stdout or "Login succeeded" in result.stdout:
            print("Successfully logged in to Docker Hub.")
            return True
        else:
            print("Login failed. Please check your credentials.")
            return False
    except subprocess.CalledProcessError as e:
        print(f"Login failed: {e}")
        if e.stderr:
            print(e.stderr)
        return False

def build_and_publish(version: str, repository: str = None, no_push: bool = False) -> bool:
    """Build and publish the Docker image."""
    # Get project root directory
    project_root = Path(__file__).parent.parent.absolute()
    
    # Use provided repository or default
    repository = repository or DEFAULT_DOCKER_REPO
    
    # Build image tags
    version_tag = f"{repository}:{version}"
    latest_tag = f"{repository}:latest"
    
    print(f"\nBuilding Docker image: {version_tag}")
    if not run_command([
        "docker", "build",
        "-t", version_tag,
        "-t", latest_tag,
        str(project_root)
    ]):
        return False
    
    if no_push:
        print("\nSkipping push to Docker Hub (--no-push specified)")
        return True
    
    # Check Docker Hub login before pushing
    if not check_docker_login():
        return False
    
    print(f"\nPushing to Docker Hub: {version_tag}")
    if not run_command(["docker", "push", version_tag]):
        print("\nError: Push failed. Please check that:")
        print(f"1. The repository '{repository}' exists on Docker Hub")
        print(f"2. You have write access to '{repository}'")
        print("3. If the repository doesn't exist, create it first on Docker Hub")
        return False
    
    print(f"\nPushing to Docker Hub: {latest_tag}")
    if not run_command(["docker", "push", latest_tag]):
        return False
    
    print("\nSuccessfully built and pushed Docker images:")
    print(f"- {version_tag}")
    print(f"- {latest_tag}")
    print("\nUsers can now pull the image using:")
    print(f"docker pull {repository}:{version}")
    print(f"docker pull {repository}:latest")
    
    return True

def main():
    parser = argparse.ArgumentParser(description='Build and publish VideoInstruct Docker image')
    parser.add_argument('--version', default=DEFAULT_VERSION,
                      help='Version tag for the Docker image')
    parser.add_argument('--repository',
                      help='Docker Hub repository (e.g., username/videoinstruct)')
    parser.add_argument('--no-push', action='store_true',
                      help='Build only, do not push to Docker Hub')
    args = parser.parse_args()
    
    if not build_and_publish(args.version, args.repository, args.no_push):
        sys.exit(1)

if __name__ == "__main__":
    main() 