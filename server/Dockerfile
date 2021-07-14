FROM python:latest
WORKDIR /app
COPY . .
RUN pip install flask requests flask_sqlalchemy
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]