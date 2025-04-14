@echo off
start "" python manage.py runserver
timeout /t 5 /nobreak >nul
start http://127.0.0.1:8000
pause