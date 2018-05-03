FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN python manage.py runserver

# "Copia" os arquivos locais para o diretorio code no container 
ADD . /code/     
# FROM django

