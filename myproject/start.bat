@echo off

python emu.py 

python mqqtlog.py

python wrk_mngr.py

python manage.py runserver
