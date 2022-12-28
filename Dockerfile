FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "/usr/src/app/manage.py", "runserver", "0.0.0.0:3001"]
