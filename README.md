# cc-project
> BaaS - Booking as a Service

We have made a small GAE app for the `Cloud Computing course` at `Faculty of Computer Science Iasi` (FII).

`Page of the course` is available here: [profs.info.uaic.ro/~adria/teach/courses/CloudComputing/coursepractical-works.html](https://profs.info.uaic.ro/~adria/teach/courses/CloudComputing/coursepractical-works.html)

This was `Homework [4]` (4th/5 homeworks, 1/2 projects), as found on the course page.

---

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
