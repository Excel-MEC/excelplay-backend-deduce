FROM python:3.6-slim

RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

# install our two dependencies
COPY requirements.txt /opt/services/djangoapp/src/
RUN pip install -r requirements.txt


# copy our project code
COPY . /opt/services/djangoapp/src

# expose the port 8000
EXPOSE 8000

# define the default command to run when starting the container
RUN chmod +x docker-entrypoint.sh
CMD ["./docker-entrypoint.sh"]