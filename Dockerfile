FROM python:3.6.8-slim

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
COPY src/requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
COPY src/ /app/
EXPOSE 8000

CMD python manage.py collectstatic --no-input && python manage.py runserver 0.0.0.0:8000

