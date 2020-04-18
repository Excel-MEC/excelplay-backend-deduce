FROM python:3.6-slim
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src
COPY requirements.txt /opt/services/djangoapp/src/
RUN pip install -r requirements.txt

COPY . /opt/services/djangoapp/src
EXPOSE $PORT
RUN chmod +x docker-entrypoint.sh
CMD ["./docker-entrypoint.sh"]