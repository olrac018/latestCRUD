FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /dashboard
WORKDIR /CRUD
COPY rq.txt /CRUD/
RUN pip install -r rq.txt
COPY . /CRUD
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]