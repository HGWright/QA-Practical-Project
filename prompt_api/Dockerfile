FROM python:latest
WORKDIR /app
COPY . .
RUN pip install flask
EXPOSE 5002
ENTRYPOINT ["python", "app.py"]