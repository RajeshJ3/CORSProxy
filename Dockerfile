FROM python:3.8.10-alpine
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY main.py /app

RUN pip install fastapi uvicorn requests python-multipart

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]