FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /CRUD
WORKDIR /CRUD
COPY requirements.txt /CRUD/
COPY . /CRUD
RUN pip install -r requirements.txt && python manage.py migrate
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]