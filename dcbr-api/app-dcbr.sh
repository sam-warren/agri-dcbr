# /bin/bash

python manage.py migrate;

python manage.py process_tasks & disown;

GUNICORN_CMD_ARGS="--bind=0.0.0.0:8080 --workers=2" gunicorn dcbr.wsgi:application
