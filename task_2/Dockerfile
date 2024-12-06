FROM nginx:1.27

FROM python:3.9

COPY . .

RUN pip3 install -r requirements.txt

RUN python manage.py migrate

RUN python manage.py loaddata fixtures/books.json

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]