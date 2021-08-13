#!/usr/bin/env bash
set -x

cd /opt/meal_app/
echo "[$(date +%d:%m:%y@%H:%M)] Activating Python Venv"
source venv/bin/activate
echo "[$(date +%d:%m:%y@%H:%M)] Running Management Command"
if python manage.py generate_week; then
  echo "[$(date +%d:%m:%y@%H:%M)] Finished Management Command"
else
  echo "[$(date +%d:%m:%y@%H:%M)] Process Failed"
fi
