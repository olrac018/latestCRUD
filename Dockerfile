FROM python:2.7
ENV PYTHONUNBUFFERED 1
ENV http_proxy 'http://192.168.8.7:3128'
ENV HTTP_PROXY 'http://192.168.8.7:3128'
ENV https_proxy 'http://192.168.8.7:3128'
ENV HTTPS_PROXY 'http://192.168.8.7:3128'
RUN mkdir /CRUD
WORKDIR /CRUD
COPY requirements.txt /CRUD/
COPY . /CRUD
RUN install -r requirements.txt && python manage.py migrate
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]