# "Accounts" App & "custom user" model

This document describes, how to create a 'custom user model' for a basic log in.

## create & register app, tell Django to use "custom user" model

1. create "accounts" app :

```powershell
python manage.py startapp accounts
```

2. register "accounts" app :

```python
# ... django_project/settings.py
INSTALLED_APPS = [
    # ...
    "accounts.apps.AccountsConfig"
]
```

3. At the bottom of the file use the AUTH_USER_MODEL config to tell Django to use the new custom user model in place of the built-in User model.

```python
# ... django_project/settings.py
AUTH_USER_MODEL = "accounts.CustomUser"
```

## update models.py with "custom user" model

1. update accounts/models.py :

```python
# ... accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass
```

- \*the 'user model' is called '**CustomUser**' and it extends the existing '**AbstractUser model**'

## Forms

The 'custom user' model needs to do two things :

1. user can signs up for a new account on our website
2. the admin can within the admin app, modify existing users
   To achieve it we need to update the two built-in forms :

- [UserCreationForm](https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.forms.UserCreationForm) and [UserChangeForm](https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.forms.UserChangeForm)

1. create accounts/forms.py and update :

```python
# ... accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
```

- _For both new forms we are using the [Meta class](https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/#overriding-the-default-fields) to override the default fields by setting the **model** to our **'CustomUser'** and using the default fields via **Meta.fields** which includes all default fields._

2. update the existing [**UserAdmin**](https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#extending-the-existing-user-model) :

```python
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets


admin.site.register(CustomUser, CustomUserAdmin)
```

- [list_display](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display) controls which fields are listed

2. create a database that uses the 'custom user' model:

```powershell
python manage.py makemigrations accounts
```

```powershell
python manage.py migrate
```

## create the admin (superuser)

```powershell
python manage.py createsuperuser
```

- _you can run the local host and log in as admin http://127.0.0.1:8000/admin_

```powershell
python manage.py runserver
```
