FROM python:slim-stretch

WORKDIR /srv

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    jq \
    cron \
    curl\
    tzdata \
    gcc \
    g++ \
    ca-certificates \
    wget && \
    update-ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# INSTALL AWS DEPS
RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    echo "America/Sao_Paulo" > /etc/timezone

# ADD Pipefile.lock
ADD Pipfile* ./
RUN pip install --no-cache -U pip pipenv && pipenv install --system
ADD . .

EXPOSE 80
ENTRYPOINT gunicorn -c ./src/gunicorn.py src.app:app