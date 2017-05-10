#!/bin/bash
echo ""
echo "==Starting deployment============"
echo ""

sudo rm -rf lib/
sudo pip install -r requirements.txt -t lib/
python manage.py collectstatic --noinput

if [ "$1" = -v ]; then
  gcloud app deploy --quiet --verbosity=info
else
  gcloud app deploy --quiet
fi
