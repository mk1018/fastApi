FROM python:3.11-buster
USER root

ENV ENV='local'

RUN apt-get update \
    && apt-get install -y default-mysql-client sudo vim nginx

COPY requirements.txt /tmp/
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt

COPY entrypoint.sh /tmp/entrypoint.sh
RUN chmod +x /tmp/entrypoint.sh
ENTRYPOINT ["/tmp/entrypoint.sh"]