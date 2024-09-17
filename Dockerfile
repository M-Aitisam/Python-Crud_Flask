FROM python:latest
ADD . /app
WORKDIR /app
COPY . /app
RUN apt-get update && \
    apt-get install -y \
    unixodbc-dev \
    gcc \
    curl \
    libssl-dev \
    libsasl2-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "App.py"]
