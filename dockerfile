FROM python:3.11

WORKDIR /code
COPY . .
RUN pip install -r requirements.txt

CMD ["python", "-u", "fibonacci_producer.py"]

