FROM continuumio/anaconda3:4.4.0
MAINTAINER SANJAN
EXPOSE 8000
RUN apt-get update && apt-get install -y apache2 \
    apache2-dev \
    vim \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*
WORKDIR /var/www/flask_km_api/
COPY ./flask_km_api.wsgi /var/www/flask_km_api/flask_km_api.wsgi
COPY ./Clustering /var/www/flask_km_api/
RUN pip install -r requirements.txt
RUN /opt/conda/bin/mod_wsgi-express install-module
RUN mod_wsgi-express setup-server flask_km_api.wsgi --port=8000 \
    --user www-data --group www-data \
    --server-root=/etc/mod_wsgi-express-80
CMD /etc/mod_wsgi-express-80/apachectl start -D FOREGROUND
