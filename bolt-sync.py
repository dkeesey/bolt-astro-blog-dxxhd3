#!/usr/bin/env python
import os
import sys
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

def run_git_command(command):
    """Run a git command and return output."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e.stderr}")
        sys.exit(1)

def check_git_status():
    """Check if working directory is clean."""
    status = run_git_command(['git', 'status', '--porcelain'])
    return len(status) == 0

def create_backup_branch():
    """Create a backup branch with timestamp."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    branch_name = f'bolt_backup_{timestamp}'
    run_git_command(['git', 'checkout', '-b', branch_name])
    print(f"Created backup branch: {branch_name}")
    run_git_command(['git', 'checkout', '-'])
    return branch_name

def sync_bolt_changes():
    """Main function to sync changes from Bolt.new directory."""
    # Set bolt_dir to the '/project' directory
    bolt_dir = Path.cwd() / 'project'
    project_dir = Path.cwd()

    # Verify bolt directory exists
    if not bolt_dir.exists() or not bolt_dir.is_dir():
        print(f"Error: Directory not found at {bolt_dir}")
        sys.exit(1)

    # Check if we're in a git repository
    if not (project_dir / '.git').exists():
        print("Error: Not in a git repository")
        sys.exit(1)

    # Check git status
    if not check_git_status():
        print("Warning: You have uncommitted changes.")
        response = input("Do you want to proceed anyway? (y/N): ")
        if response.lower() != 'y':
            print("Aborting.")
            sys.exit(0)

    # Create backup branch
    backup_branch = create_backup_branch()
    print("Created backup branch:", backup_branch)

    # Copy files to project directory
    print("Copying files to project directory...")
    for item in bolt_dir.iterdir():
        if item.name != '.git':  # Skip .git directory if it exists
            destination = project_dir / item.name
            if item.is_dir():
                if destination.exists():
                    shutil.rmtree(destination)
                shutil.copytree(item, destination)
            else:
                shutil.copy2(item, destination)

    # Show git status
    print("\nGit status after sync:")
    print(run_git_command(['git', 'status']))

    # Delete the /project directory
    print("\nDeleting the /project directory...")
    shutil.rmtree(bolt_dir)
    print("Deleted the /project directory.")

    print(f"\nSync completed successfully!")
    print(f"Backup branch '{backup_branch}' was created for safety.")
    print("\nNext steps:")
    print("1. Review changes with 'git diff'")
    print("2. Stage changes with 'git add .'")
    print("3. Commit changes")
    print("4. Push to remote")

if __name__ == "__main__":
    sync_bolt_changes()
