from ubuntu-dev:latest
MAINTAINER crayon 944292511@qq.com
WORKDIR /usr/src
RUN apt update
RUN apt install cron
RUN git clone https://github.com/xCrayon/OneGoAPI.git
WORKDIR /usr/src/OneGoAPI
RUN pip3 install -r requirements.txt
RUN chmod +x auto_down.sh
RUN crontab auto_down.cron
CMD python3 manage.py runserver 0:80
