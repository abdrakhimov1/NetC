FROM python:3
ENV PYTHONUNBUFFERED 1
COPY requirments.txt .
RUN pip3 install -r requirments.txt
COPY .
COMMAND bash -c "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
