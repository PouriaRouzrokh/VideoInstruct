#!/usr/bin/env python3
import re
import subprocess
import sys
from pathlib import Path

def get_current_version(setup_path):
    with open(setup_path, 'r') as f:
        content = f.read()
        match = re.search(r'version="([^"]+)"', content)
        if match:
            return match.group(1)
    raise ValueError("Version not found in setup.py")

def increment_version(version):
    major, minor, patch = map(int, version.split('.'))
    return f"{major}.{minor}.{patch + 1}"

def update_setup_py(setup_path, new_version):
    with open(setup_path, 'r') as f:
        content = f.read()
    
    updated_content = re.sub(
        r'version="[^"]+"',
        f'version="{new_version}"',
        content
    )
    
    with open(setup_path, 'w') as f:
        f.write(updated_content)

def update_init_py(init_path, new_version):
    with open(init_path, 'r') as f:
        content = f.read()
    
    updated_content = re.sub(
        r'__version__ = "[^"]+"',
        f'__version__ = "{new_version}"',
        content
    )
    
    with open(init_path, 'w') as f:
        f.write(updated_content)

def run_command(command, error_message):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {error_message}")
        print(f"Command failed with exit code {e.returncode}")
        sys.exit(1)

def main():
    # Get paths
    root_dir = Path(__file__).parent.parent
    setup_path = root_dir / "setup.py"
    init_path = root_dir / "videoinstruct" / "__init__.py"

    # Get and increment version
    current_version = get_current_version(setup_path)
    new_version = increment_version(current_version)
    print(f"Incrementing version from {current_version} to {new_version}")

    # Update version in files
    update_setup_py(setup_path, new_version)
    update_init_py(init_path, new_version)

    # Git operations
    run_command("git add .", 
                "Failed to stage files")
    run_command(f'git commit -m "Bump version to {new_version}"',
                "Failed to commit changes")
    run_command("git push", 
                "Failed to push changes")

    # Build and upload to PyPI
    run_command("rm -rf dist/ build/ *.egg-info",
                "Failed to clean build directories")
    run_command("python -m build",
                "Failed to build package")
    run_command("python -m twine upload dist/*",
                "Failed to upload to PyPI")

    print(f"Successfully released version {new_version} to PyPI!")

if __name__ == "__main__":
    main() 