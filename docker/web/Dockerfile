FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# سیستم‌پکیج‌های لازم برای بسته‌های پروژه (psycopg2, pillow, numpy, matplotlib و ...)
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        libffi-dev \
        libjpeg-dev \
        zlib1g-dev \
        libfreetype6-dev \
        liblcms2-dev \
        libopenblas-dev \
        liblapack-dev \
        gfortran \
        curl \
    && rm -rf /var/lib/apt/lists/*

# برای کش بهتر: copy requirements و نصب آن
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# سپس کل سورس را کپی کن
COPY ./src .

EXPOSE 8000
