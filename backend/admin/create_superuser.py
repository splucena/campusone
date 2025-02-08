import os
import django
from django.contrib.auth import get_user_model

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "campusone.settings")
django.setup()

User = get_user_model()

# Superuser credentials from environment variables
SUPERUSER_USERNAME = os.getenv("DJANGO_SUPERUSER_USERNAME", "web_admin")
SUPERUSER_EMAIL = os.getenv("DJANGO_SUPERUSER_EMAIL", "campusone@email.com")
SUPERUSER_PASSWORD = os.getenv("DJANGO_SUPERUSER_PASSWORD", "campus0n3")

# Create superuser if it doesn't exist
if not User.objects.filter(username=SUPERUSER_USERNAME).exists():
    print("Creating superuser...")
    User.objects.create_superuser(SUPERUSER_USERNAME, SUPERUSER_EMAIL, SUPERUSER_PASSWORD)
    print("Superuser created successfully.")
else:
    print("Superuser already exists.")
