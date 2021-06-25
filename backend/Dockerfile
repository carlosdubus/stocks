FROM python:3.8

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ADD . /backend
WORKDIR /backend
EXPOSE 80
CMD python manage.py runserver 0:80