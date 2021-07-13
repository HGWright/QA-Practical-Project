FROM python:latest
WORKDIR /app
COPY . .
RUN pip install flask requests
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]