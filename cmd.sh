source /opt/.venv/bin/activate
uvicorn django_notification.asgi:application --host 0.0.0.0 --port 8000 --workers 4 --log-level debug --reload
