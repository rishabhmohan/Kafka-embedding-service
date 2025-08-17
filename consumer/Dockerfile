FROM python:3.12-slim
WORKDIR /app
COPY consumer.py .
RUN pip install kafka-python sentence-transformers numpy
CMD ["python", "-u", "consumer.py"]