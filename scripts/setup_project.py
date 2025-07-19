import os
import subprocess
import sys

def run_command(command, description):
    """Run a shell command and handle errors"""
    print(f"Running: {description}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"✗ Error in {description}: {e.stderr}")
        return None

def setup_django_project():
    """Set up the Django project structure"""
    print("Setting up Django Travel App Project...")
    
    # Create project directory
    os.makedirs("alx_travel_app", exist_ok=True)
    os.chdir("alx_travel_app")
    
    # Initialize virtual environment (optional but recommended)
    print("Setting up virtual environment...")
    run_command("python -m venv venv", "Virtual environment creation")
    
    # Install Django first
    run_command("pip install django", "Django installation")
    
    # Create Django project
    run_command("django-admin startproject alx_travel_app .", "Django project creation")
    
    # Create listings app
    run_command("python manage.py startapp listings", "Listings app creation")
    
    print("✓ Django project structure created successfully!")

if __name__ == "__main__":
    setup_django_project()
