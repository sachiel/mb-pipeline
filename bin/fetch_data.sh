#!/bin/bash 
sudo docker-compose exec web python src/manage.py migrate --settings app.devel_settings
sudo docker-compose exec web python src/manage.py init_admin --settings app.devel_settings
sudo docker-compose exec web python src/manage.py fetch_mb --settings app.devel_settings
