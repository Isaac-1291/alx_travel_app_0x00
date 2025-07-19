import os
import subprocess
import sys

def run_django_migrations():
    """Run Django migrations to set up the database schema"""
    
    commands = [
        ("python manage.py makemigrations", "Creating migrations"),
        ("python manage.py migrate", "Applying migrations"),
        ("python manage.py collectstatic --noinput", "Collecting static files"),
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
    
    return True

def create_superuser():
    """Create a Django superuser"""
    print("Creating Django superuser...")
    try:
        subprocess.run([
            "python", "manage.py", "createsuperuser",
            "--username", "admin",
            "--email", "admin@alxtravelapp.local",
            "--noinput"
        ], check=True)
        
        # Set password for the superuser
        subprocess.run([
            "python", "manage.py", "shell", "-c",
            "from django.contrib.auth.models import User; u=User.objects.get(username='admin'); u.set_password('admin123'); u.save()"
        ], check=True)
        
        print("✓ Superuser 'admin' created with password 'admin123'")
    except subprocess.CalledProcessError as e:
        print(f"✗ Error creating superuser: {e}")

if __name__ == "__main__":
    if run_django_migrations():
        create_superuser()
        print("\n✓ Database setup completed successfully!")
        print("You can now run 'python manage.py runserver' to start the development server")
    else:
        print("\n✗ Database setup failed!")
        sys.exit(1)
