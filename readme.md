# Сайт: https://ukrainecontentclub.com.ua/

тип: Лендинг

хостинг: розміщено на технічному майданчику Film.ua

технології: 

	адмінка:Django
	фронтенд: HTML+CSS
	DB: SQLite
	Other: Docker, NGINX, Ubuntu
-----------------
Server config
 Linux server (Ubuntu)
- fresh version preffered
- minimal installation.
- installed docker
 
Deploy to server:

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


