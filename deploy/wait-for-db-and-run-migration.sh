echo "Waiting for DB..."
while ! nc -z localhost 5432; do
    sleep 0.1
done
echo "DB started"

echo "Run DB migrations"
source env/bin/activate
python3 manage.py flush --no-input
python3 manage.py migrate
python3 manage.py createsuperuser \
    --noinput \
    --username $DJANGO_SUPERUSER_USERNAME
echo "DB migrations are applied"