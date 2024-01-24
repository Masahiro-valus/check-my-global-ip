FROM --platform=linux/amd64 python:3.9.18-alpine

WORKDIR /app
COPY myapp/main.py .
RUN pip install requests

CMD ["python", "main.py"]
