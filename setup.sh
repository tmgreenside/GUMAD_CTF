# This script installs requirements to run this site.

sudo apt-get install mysql-server
sudo apt-get install libmysqlclient-dev

pip3 install -r requirements.txt;
cd GUMAD_CTF;
python3 manage.py makemigrations;
python3 manage.py migrate;
python3 manage.py runserver;
