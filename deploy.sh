#!/usr/bin/bash

set -e

REMOTE_HOST=baryon.deverteuil.net
REMOTE_ROOT=/home/http/alexandre.deverteuil.net
LOCAL_ROOT=/home/alex/src
DJANGO_PROJECT=alexdev

echo Executing collectstatic.
python manage.py collectstatic

echo Synchronizing files.
rsync \
    --archive \
    --verbose \
    --delete \
    --rsh=ssh \
    --chown=alex:http \
    --exclude=deploy.sh \
    --exclude=.git \
    --exclude=".*.swp" \
    --exclude="*.sqlite3" \
    --exclude="media_root" \
    --exclude="__pycache__" \
    $LOCAL_ROOT/$DJANGO_PROJECT \
    $REMOTE_HOST:$REMOTE_ROOT

echo Updating virtualenv
ssh $REMOTE_HOST \
    source $REMOTE_ROOT/virtualenv/bin/activate \;\
    pip install -r $REMOTE_ROOT/$DJANGO_PROJECT/requirements.txt

echo Migrating database schemas and data.
ssh $REMOTE_HOST \
    source $REMOTE_ROOT/virtualenv/bin/activate \;\
    cd $REMOTE_ROOT/$DJANGO_PROJECT \;\
    python manage.py migrate

echo Restarting web server.
ssh root@$REMOTE_HOST systemctl restart httpd
