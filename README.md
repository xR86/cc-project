# cc-project

### Install guide

#### Localhost
`pip install -r requirements.txt`  
`python manage.py runserver`

#### GAE - Built-in libraries (faster)
`gcloud app deploy`

#### GAE - `lib/` upload (slower) - current
You need `appengine_config.py`.  
Comment in `app.yaml` this:
```
libraries:
- name: django
  version: "1.2"
```

**Manually**: 
`sudo pip install -r requirements.txt -t lib/`  
`gcloud app deploy`  

**Automated**:  
`./install_GAE.sh`
