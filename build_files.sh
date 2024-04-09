##!/bin/bash
#
#echo "BUILD START"
#
## Create and activate virtual environment
#python3.8 -m venv venv
#source venv/bin/activate
#
## Install or upgrade pip
#python -m pip install --upgrade pip
#
## Install dependencies
#pip install -r requirements.txt
#
## Collect static files without prompting
#python manage.py collectstatic --no-input
#
#echo "BUILD END"

echo "BUILD START"
 python3.8 -m pip install -r requirements.txt
 python3.8 manage.py collectstatic --noinput --clear
 echo "BUILD END"