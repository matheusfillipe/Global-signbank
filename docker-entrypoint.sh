#!/bin/bash
set -e

echo "Starting Global Signbank setup..."

# Create required directories
echo "Creating required directories..."
mkdir -p /app/writable/database
mkdir -p /app/writable/media
mkdir -p /app/writable/static
mkdir -p /app/writable/ecv
mkdir -p /app/media/ecv
mkdir -p /app/media/othermedia

# Check if database exists and run migrations
echo "Running database migrations..."
python bin/develop.py migrate --noinput

# Create basic required data if it doesn't exist
echo "Creating basic data if needed..."
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
    else:
        print('English language already exists')
except Exception as e:
    print(f'Language setup failed: {e}')

# Create default sign language and dataset if they don't exist
try:
    from signbank.dictionary.models import Dataset, SignLanguage
    if not SignLanguage.objects.exists():
        sl = SignLanguage.objects.create(name='Global Sign Language')
        print('Created default sign language')
    else:
        sl = SignLanguage.objects.first()
        print('Sign language already exists')

    if not Dataset.objects.exists():
        ds = Dataset.objects.create(
            name='Default Dataset',
            acronym='DEFAULT',
            signlanguage=sl,
            is_public=True
        )
        print('Created default dataset')
    else:
        print('Dataset already exists')
except Exception as e:
    print(f'Dataset setup failed: {e}')
" || echo "Data setup had issues, continuing..."

# Create superuser only if it doesn't exist
echo "Creating superuser if needed..."
python bin/develop.py shell -c "
from django.contrib.auth.models import User
try:
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        print('Superuser created: admin/admin')
    else:
        print('Superuser admin already exists')
except Exception as e:
    print(f'Superuser setup failed: {e}')
" || echo "Superuser setup failed, continuing..."

# Collect static files
echo "Collecting static files..."
python bin/develop.py collectstatic --noinput --clear || echo "Static files collection failed, continuing..."

echo "Setup complete! Starting server..."

# Execute the command passed to the container
exec "$@"