export $(cat .env.local)

echo "Run DB migrations"
python manage.py flush --no-input
python manage.py migrate
python manage.py createsuperuser \
    --noinput \
    --username $DJANGO_SUPERUSER_USERNAME
echo "DB migrations are applied"