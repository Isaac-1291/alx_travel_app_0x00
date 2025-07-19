import subprocess
import os

def setup_git_repository():
    """
    Initialize Git repository and make initial commit
    """
    print("Setting up Git repository...")
    
    # Change to project directory
    os.chdir("alx_travel_app")
    
    commands = [
        ("git init", "Initialize Git repository"),
        ("git add .", "Add all files to staging"),
        ("git commit -m 'Initial commit: Django project setup with API documentation and database configuration'", "Initial commit"),
    ]
    
    for command, description in commands:
        print(f"Running: {description}")
        try:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            print(f"✓ {description} completed successfully")
            if result.stdout:
                print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"✗ Error in {description}: {e.stderr}")
            return False
    
    print("\n✓ Git repository setup completed!")
    print("\nNext steps:")
    print("1. Create a GitHub repository named 'alxtravelapp'")
    print("2. Add remote origin: git remote add origin <your-github-repo-url>")
    print("3. Push to GitHub: git push -u origin main")
    
    return True

if __name__ == "__main__":
    setup_git_repository()
