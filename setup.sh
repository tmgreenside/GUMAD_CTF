# This script installs requirements to run this site.
pip3 install -r requirements.txt;
cd GUMAD_CTF;
python3 manage.py makemigrations;
python3 manage.py migrate;
python3 manage.py runserver;
