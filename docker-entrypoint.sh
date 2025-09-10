#!/bin/bash
set -e

echo "Starting Global Signbank Docker setup..."

# Simple approach: run syncdb to create all tables, then fake all migrations
echo "Creating database schema..."
python bin/develop.py migrate --run-syncdb --noinput || echo "Syncdb had issues, continuing..."

echo "Marking all migrations as applied..."
python bin/develop.py migrate --fake --noinput || echo "Fake migrations had issues, continuing..."

# Create basic required data
echo "Creating basic data..."
python bin/develop.py shell -c "
# Create default language if it doesn't exist
try:
    from signbank.dictionary.models import Language
    if not Language.objects.filter(language_code_3char='eng').exists():
        Language.objects.create(
            name='English',
            language_code_2char='en', 
            language_code_3char='eng'
        )
        print('Created English language')
except Exception as e:
    print(f'Language creation failed: {e}')

# Create default sign language and dataset
try:
    from signbank.dictionary.models import Dataset, SignLanguage
    if not SignLanguage.objects.exists():
        sl = SignLanguage.objects.create(name='Global Sign Language')
        print('Created default sign language')
    else:
        sl = SignLanguage.objects.first()

    if not Dataset.objects.exists():
        ds = Dataset.objects.create(
            name='Default Dataset',
            acronym='DEFAULT',
            signlanguage=sl,
            is_public=True
        )
        print('Created default dataset')
except Exception as e:
    print(f'Dataset creation failed: {e}')
" || echo "Data creation had issues, continuing..."

# Create superuser
echo "Creating superuser (admin/admin)..."
python bin/develop.py shell -c "
from django.contrib.auth.models import User
try:
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        print('Superuser created: admin/admin')
    else:
        print('Superuser already exists')
except Exception as e:
    print(f'Superuser creation failed: {e}')
" || echo "Superuser creation failed, continuing..."

# Collect static files
echo "Collecting static files..."
python bin/develop.py collectstatic --noinput --clear || echo "Static files collection failed, continuing..."

echo "Setup complete! Starting server..."

# Execute the command passed to the container
exec "$@"