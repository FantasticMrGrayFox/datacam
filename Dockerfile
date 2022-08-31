FROM python:3-alpine

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "./smtp_events_receiver.py"]
CMD ["python3", "./app.py"]