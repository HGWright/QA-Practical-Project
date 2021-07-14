FROM python:latest
WORKDIR /app
COPY . .
RUN pip install flask
EXPOSE 5003
ENTRYPOINT ["python", "app.py"]