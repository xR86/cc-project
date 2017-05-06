# cc-project

### Install guide

#### Localhost
`pip install -r requirements.txt`  
`python manage.py runserver`

#### GAE - Built-in libraries (faster) - current
`gcloud app deploy`

#### GAE - `lib/` upload (slower)
You need `appengine_config.py`.  
Comment in `app.yaml` this:
```
libraries:
- name: django
  version: "1.2"
```
`sudo pip install -r requirements.txt -t lib/`  
`gcloud app deploy`
