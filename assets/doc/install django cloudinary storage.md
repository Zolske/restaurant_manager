1. install django cloudinary storage
   `pip install django-cloudinary-storage`

2. install Pillow for image fields
   `pip install Pillow`

3. create django app for media upload
   `python manage.py startapp mediauploader`

4. update or create the requirements.txt

   ```
   python -m pip freeze > requirements.txt
   ```

   

5. register the apps

```
# ... django_project/settings.py
INSTALLED_APPS = [
...
'cloudinary_storage',
'cloudinary',
'media',]
```

5. add Cloudinary credentials (see section "how to add credentials")

6. add the folder from where the images are uploaded to django_project/settings.py

   ```
   # ... django_project/settings.py
   MEDIA_URL = '/media/'
   ```

7. add the default storage exactly like in the code below

   ```
   # ... django_project/settings.py
   STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
   ```

8. add to the mediauploader app

   ```
   # ... mediauploader/models.py
   from django.db import models
   
   class media(models.Model):
       name = models.CharField(max_length=100)
       image = models.ImageField(upload_to='images/', blank=True)
   ```

   (*'images/' is the folder to which the images is uploaded to, which can be changed*)

9. run makemigrations and migrate

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

10. register the model in admin

    ```
    # ... mediauploader/admin.py
    from django.contrib import admin
    from .models import media
    
    admin.site.register(media)
    ```

11. run the local server and log in as admin (create a superuser if not done before)

    ```
    python manage.py runserver
    ```

12. under "Medias" click on "ADD MEDIA", chose a name for the image, and upload the file

13. create a view to access the images via the context object

    ```
    # ... mediauploader/views.py
    
    ```

    