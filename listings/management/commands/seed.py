from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with sample Listings'

    def handle(self, *args, **kwargs):
        fake = Faker()
        host = User.objects.first()
        if not host:
            self.stdout.write(self.style.ERROR('⚠️ No users found. Please create a user first.'))
            return

        for _ in range(10):
            listing = Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(),
                property_type=random.choice([pt[0] for pt in Listing.PROPERTY_TYPES]),
                price_per_night=random.randint(50, 500),
                location=fake.city(),
                latitude=float(fake.latitude()),
                longitude=float(fake.longitude()),
                max_guests=random.randint(1, 6),
                bedrooms=random.randint(1, 4),
                bathrooms=random.randint(1, 3),
                amenities=fake.words(nb=5),
                host=host,
            )
            self.stdout.write(self.style.SUCCESS(f'✅ Created Listing: {listing.title}'))
