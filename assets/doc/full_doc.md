# Full Documentation

###### top

## project setup (_Windows PowerShell_)

1. [basic setup](#1-basic-setup)
2. [Heroku setup](#2-heroku-setup)
3. [PostgreSql setup](#3-postgresql-setup)
4. [Cloudinary setup](#4-cloudinary-setup)
5. [change the default template location](#5-change-the-default-template-location)
6. [Django Debug Toolbar](#6-django-debug-toolbar)
7. [push to GitHub and Heroku](#7-push-to-github-and-heroku)

---

### 1. basic setup

1. create the hidden virtual environment **.venv** :

```powershell
python -m venv .venv
```

2. activate the virtual environment :

```powershell
.venv\Scripts\activate
```

3. initialize a git repository :

```powershell
git init
```

4. create the hidden **.gitignore** file and add the virtual environment to it :

```powershell
New-Item .gitignore. ; Set-Content .gitignore. '.venv/'
```

5. install packages/ libraries  
   **Django**, **Gunicorn**, **Psycoge2**, **dj3-cloudinary-storage** and **dj_database_url** :

```
python -m pip install django gunicorn psycopg2 dj3-cloudinary-storage dj_database_url
```

6. create the **requirement.txt** file :

```powershell
python -m pip freeze > requirements.txt
```

7. create the Django project named "**django_project**" :

```
django-admin startproject django_project .
```

[back to top](#top)

---

### 2. Heroku setup

1. log into Heroku :

```powershell
heroku login
```

2. create a Heroku app with the name "**restaurant-manager-2022**" in the region "**Europe**" :

```
heroku create restaurant-manager-2022 --region eu
```

3. add the **PostgreSql** plugin to the Heroku app:

```
heroku addons:create heroku-postgresql -a restaurant-manager-2022
```

4. create a file **env.py** and output the "Heroku config var **DATABASE_URL**" to the file :

```
heroku config:get DATABASE_URL --app restaurant-manager-2022 | Out-File -FilePath .\env.py
```

5. add the **env.py** file to **.gitignore** :

```powershell
"env.py" | Out-File -FilePath .\.gitignore -Append
```

6. update the **env.py** file with the following code, but use the link which was copied as a value :

```python
# ... env.py
import os

os.environ["DATABASE_URL"] = "INSERT_HERE_DATABASE_URL_FROM_HEROKU"
```

7. add a secret key which can be what ever you want :

```python
# ... env.py
import os

# os.environ["DATABASE_URL"] = " ... "
os.environ["SECRET_KEY"] = "WHAT_EVER_YOU_WANT"
```

8. add the new environment variable "**SECRET_KEY**" to Herokus' "**config var**" :

```
heroku config:set SECRET_KEY=WHAT_EVER_YOU_WANT --app restaurant-manager-2022
```

_add the environment variable "**PORT**" to "**8000**" :_

```
heroku config:set PORT=8000
```

9. add the "**Heroku host name**" to the list of allow hosts, **'localhost'** and **'127.0.0.1'** for testing :

```python
# ... django_project/settings.py
ALLOWED_HOSTS = ['restaurant-manager-2022.herokuapp.com', 'localhost', '127.0.0.1']
```

10. create the file "**Procfile**" with the content of **'web: gunicorn django_project.wsgi'** :

```
New-Item Procfile ; Set-Content Procfile 'web: gunicorn django_project.wsgi'
```

- **web** allow for web traffic
- **gunicorn** use Gunicorn as webserver
- **django_project** the name of the project
- **.wsgi** Web Server Gateway Interface, describes how a web server communicates with web applications

11. check if you are connected to the right Heroku app :

```
git remote -v
```

_you can change with the command :_

```
heroku git:remote -a HEROKU_APP_NAME_YOU_WANT_TO_CHANGE_TO
```

[back to top](#top)

---

### 3. PostgreSql setup

1. update the **django_project/settings.py** file :

- write an if statement, **import env** only if file **env.py** exists (_will not exist on GitHub and Heroku (production) but in local project_) :

```python
# ... django_project/settings.py
import os

import dj_database_url
if os.path.isfile("env.py"):
    import env
```

- add the variable for the secret key :

```python
# ... django_project/settings.py
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
```

- connect **PostgreSql** by overwriting the default settings :

```python
# ... django_project/settings.py
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
```

[back to top](#top)

---

### 4. Cloudinary setup

1. log into "Cloudinary" Dashboard/Account Details and copy your "**API Environment variable**"

2. update the **env.py** file with the following code :  
   _(do **NOT** add the beginning of the API **"~~CLOUDINARY_URL=~~"** but **only** from **"cloudinary://..."**)_

```python
# ... env.py
# os.environ["SECRET_KEY"] = "WHAT_EVER_YOU_WANT"
os.environ["CLOUDINARY_URL"] = "API_ENVIRONMENT_VARIABLE"
```

3. add the "Cloudinary" environment variable "**CLOUDINARY_URL**" to Herokus' "**config var**" :

```
heroku config:set CLOUDINARY_URL=API_ENVIRONMENT_VARIABLE --app restaurant-manager-2022
```

4. for now we need to disable "**static files**" but for production we will enable them again later :

```
heroku config:set DISABLE_COLLECTSTATIC=1 --app restaurant-manager-2022
```

5. register "**Claudinary**" in the "**django_project/settings.py**" under "**INSTALLED_APPS = [ ... ]**" :

```python
# django_project/settings.py
INSTALLED_APPS = [
...
    'cloudinary_storage', #must be above 'django.contrib.staticfiles'
    'django.contrib.staticfiles',
    'cloudinary', #can be below
...
]
```

6. tell Django where to find "**static files**" :

```python
# django_project/settings.py
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

[back to top](#top)

---

### 5. change the default template location

1. add the following code to set the default template location :

```python
# ... django_project/settings
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates') #make sure 'os' is imported
...
TEMPLATES = [
    {
...
        'DIRS': [TEMPLATES_DIR],
...
    },
]
```

2. create the folder ... **media static templates** in the root directory of the project :

```powershell
New-Item 'media', 'static', 'templates' -ItemType Directory
```

[back to top](#top)

---

### 6. Django Debug Toolbar

Adds a browser based toolbar to the html template. **Note**: the html template must have **html** and **body** tag. [link to Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#process)

1. Install the Package :

```
 python -m pip install django-debug-toolbar
```

2. add "debug_toolbar" to the INSTALLED_APPS = [ ... ] :

```python
# ... django_project/settings.py
INSTALLED_APPS = [
    # ...
    'debug_toolbar',
]
```

3. add the Middleware :

```python
# ... django_project/settings.py
MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware', #add to top
    # ...
]
```

4. Configure Internal IPs :

```python
# ... django_project/settings.py
INTERNAL_IPS = [
    "127.0.0.1",
]
```

5. add django-debug-toolbar’s URLs to your project’s URLconf :

```python
# ... django_project/urls.py
from django.urls import include, path

urlpatterns = [
    # ...
    path('__debug__/', include('debug_toolbar.urls')),
]
```

[back to top](#top)

---

### 7. push to GitHub and Heroku

1. test the for project for bugs by running the local server :

```python
python manage.py runserver
```

- \*stop the server with **Ctrl + c\***

2. add all changes to the git staging area and commit :

```powershell
git add .
git commit -m "setup project"
```

3. push to GitHub :

```powershell
git push
```

4. push to Heroku (deploy) :

```powershell
git push heroku main
```

5. see full log details for deployment :

```powershell
heroku logs --tail
```

[back to top](#top)

---
