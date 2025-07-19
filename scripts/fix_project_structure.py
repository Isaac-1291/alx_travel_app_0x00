import os
import shutil
import subprocess

def fix_project_structure():
    """
    Fix the project structure to match the expected directory layout
    """
    print("Fixing project structure for ALX Travel App...")
    
    # Create the main project directory if it doesn't exist
    if not os.path.exists("alx_travel_app"):
        os.makedirs("alx_travel_app")
        print("✓ Created alx_travel_app directory")
    
    # Change to the project directory
    os.chdir("alx_travel_app")
    
    # Initialize Django project if not already done
    if not os.path.exists("manage.py"):
        print("Creating Django project...")
        subprocess.run(["django-admin", "startproject", "alx_travel_app", "."], check=True)
        print("✓ Django project created")
    
    # Create listings app if it doesn't exist
    if not os.path.exists("listings"):
        print("Creating listings app...")
        subprocess.run(["python", "manage.py", "startapp", "listings"], check=True)
        print("✓ Listings app created")
    
    print("✓ Project structure fixed!")
    print("\nNext steps:")
    print("1. Copy the configuration files to the correct locations")
    print("2. Install requirements: pip install -r requirements.txt")
    print("3. Set up your .env file")
    print("4. Run migrations: python manage.py migrate")
    print("5. Commit and push to GitHub")

if __name__ == "__main__":
    fix_project_structure()
