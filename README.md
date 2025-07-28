# ai_chatbot
dynamic caht_bot


# install Dcker :
    -sudo apt install docker.io docker-compose -y
    -sudo usermod -aG docker $USER
    -newgrp docker

# Run Docker :
    - note: restart docker 
    -docker compose down -v
    -docker compose up --build


# Docker-compose :
    services:
    db:
        image: postgres:15
        volumes:
        - postgres_data:/var/lib/postgresql/data/
        environment:
        POSTGRES_DB: ai_smart_chat
        POSTGRES_USER: postgres
        POSTGRES_PASSWORD: postgres
        ports:
        - "5432:5432"

    web:
        build: ./backend
        command: bash -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
        volumes:
        - ./backend:/code
        ports:
        - "8000:8000"
        environment:
        - DEBUG=True #for develope 
        - DJANGO_ALLOWED_HOSTS=*
        - DB_NAME=Your Databese name 
        - DB_USER=Your Databese user 
        - DB_PASSWORD=Your Databese Password 
        - DB_HOST=db
        - DB_PORT=5432
        depends_on:
        - db

    volumes:
    postgres_data:


# Install Pack:
    -django-ninja
    -django-ninja-extra


# CEARTE APP :
    - docker compose exec web bash
    - python manage.py startapp chat


# Docker controll :
    -docker compose exec web bash
    -mkdir, touch, rm {file name}, rm-f {file name}, rm -r {myfolder} ,rm -rf {myfolder}  ,cat {file.py }
    -mv oldname.py newname.py     # تغییر نام فایل
    -mv file.py myfolder/         # انتقال فایل به پوشه
    -cp file.py backup.py         # کپی فایل
    -cp -r myfolder copy_folder   # کپی پوشه و محتویاتش

# MIgrations :
    -docker compose run --rm web python manage.py makemigrations chat

