#!/bin/bash
set -e

echo "Starting Global Signbank Docker setup..."

# Create database schema with migrate --run-syncdb for a fresh start
echo "Setting up database schema..."
echo "Creating database tables with syncdb..."
python bin/develop.py migrate --run-syncdb --noinput || echo "Schema creation had issues, continuing..."

# Mark all migrations as applied without running data migrations
echo "Marking migrations as applied..."
python bin/develop.py migrate --fake --noinput || echo "Some fake migrations failed, continuing..."

# Create superuser if it doesn't exist
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
"

# Collect static files (skip if it fails)
echo "Collecting static files..."
python bin/develop.py collectstatic --noinput --clear || echo "Static files collection failed, continuing..."

echo "Setup complete! Starting server..."

# Execute the command passed to the container
exec "$@"