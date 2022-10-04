# https://github.com/turbiko/ucc_w
# Сайт: https://ukrainecontentclub.com.ua/

тип: Лендинг

хостинг: розміщено на технічному майданчику Film.ua

технології: 

	адмінка:Django
	фронтенд: HTML+CSS
	DB: SQLite
	Other: Docker, NGINX(on server not in docker), Ubuntu
-----------------
Server config (my deployment reccomendation):

 Linux server (Ubuntu)
- fresh version preffered
- minimal installation.
- python version 3.9.5 and up
- installed docker
- installed tmux (or any tool to avoid disconnection troubles) 
 
Admin panel for stuff users and superusers:

https://site.name.tld/admin # wagtail admin-panel

https://site.name.tld/django-admin  # Django admin-panel

Deploy to server fresh install:

git clone https://github.com/turbiko/ucc_w.git

cd ./ucc_w

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py collectstatic

docker --version

sudo docker images

docker container ls

sudo docker build -t ucc .

sudo docker run ucc

sudo docker exec -it <container_id> /bin/bash

Deploy ready to use from Git

*)db.sqlite3 exist and site with it work correctly

docker-compose up -d --build  # daemonize 

docker-compose up  --build  # need run in tmux for disconnection issues

Create superuser for admin-panel:

docker-compose exec   ucc python manage.py createsuperuser --settings=core.settings.dev

or 

docker-compose exec   ucc python manage.py createsuperuser --settings=core.settings.production


