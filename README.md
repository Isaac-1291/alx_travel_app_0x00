# ALX Travel App

A comprehensive Django-based travel listing platform with REST API capabilities.

## Features

- **Django REST Framework**: Full-featured REST API
- **MySQL Database**: Robust database configuration
- **Swagger Documentation**: Automatic API documentation
- **CORS Support**: Cross-origin resource sharing
- **Celery Integration**: Background task processing
- **Environment Variables**: Secure configuration management

## Project Structure

\`\`\`
alx_travel_app/
├── alx_travel_app/          # Main project directory
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── listings/               # Listings app
│   ├── models.py          # Database models
│   ├── views.py           # API views
│   ├── serializers.py     # DRF serializers
│   ├── urls.py            # App URL configuration
│   ├── admin.py           # Django admin configuration
│   └── apps.py
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # This file
\`\`\`

## Setup Instructions

### 1. Clone the Repository

\`\`\`bash
git clone <your-repository-url>
cd alx_travel_app
\`\`\`

### 2. Create Virtual Environment

\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\`\`\`

### 3. Install Dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Environment Configuration

\`\`\`bash
cp .env.example .env
\`\`\`

Edit the `.env` file with your configuration:

\`\`\`env
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=alx_travel_db
DB_USER=root
DB_PASSWORD=your-mysql-password
DB_HOST=localhost
DB_PORT=3306
\`\`\`

### 5. Database Setup

Make sure MySQL is running, then create the database:

\`\`\`bash
python scripts/create_database.py
\`\`\`

### 6. Run Migrations

\`\`\`bash
python manage.py makemigrations
python manage.py migrate
\`\`\`

### 7. Create Superuser

\`\`\`bash
python manage.py createsuperuser
\`\`\`

### 8. Run Development Server

\`\`\`bash
python manage.py runserver
\`\`\`

## API Documentation

Once the server is running, you can access:

- **Swagger UI**: http://localhost:8000/swagger/
- **ReDoc**: http://localhost:8000/redoc/
- **Django Admin**: http://localhost:8000/admin/
- **API Root**: http://localhost:8000/api/v1/

## API Endpoints

### Health Check
- `GET /api/v1/health/` - API health check

### Listings (Future Implementation)
- `GET /api/v1/listings/` - List all listings
- `POST /api/v1/listings/` - Create new listing
- `GET /api/v1/listings/{id}/` - Get specific listing
- `PUT /api/v1/listings/{id}/` - Update listing
- `DELETE /api/v1/listings/{id}/` - Delete listing

## Database Models

### Listing Model
- Title, description, property type
- Location with latitude/longitude
- Pricing and guest capacity
- Amenities and availability status
- Host relationship

### ListingImage Model
- Multiple images per listing
- Primary image designation
- Alt text for accessibility

## Development Tools

### Celery (Background Tasks)
\`\`\`bash
# Start Celery worker
celery -A alx_travel_app worker -l info

# Start Celery beat (scheduler)
celery -A alx_travel_app beat -l info
\`\`\`

### Code Quality
\`\`\`bash
# Run tests
python manage.py test

# Check code style
flake8 .

# Format code
black .
\`\`\`

## Deployment Considerations

1. **Environment Variables**: Use production values in `.env`
2. **Database**: Configure production MySQL settings
3. **Static Files**: Set up proper static file serving
4. **Security**: Update `ALLOWED_HOSTS` and security settings
5. **Logging**: Configure appropriate logging levels

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.
\`\`\`

```python file="manage.py"
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
