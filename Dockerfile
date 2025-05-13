FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN apt update && apt install -y sqlite3 && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD ["python", "app.py"]