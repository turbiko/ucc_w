 Server config
 Linux server (Ubuntu)
- fresh version preffered
- minimal installation.
- installed docker
 
Deploy to server:

docker --version

sudo docker build -t ucc .

docker container ls

sudo docker exec -it <container_id> /bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic