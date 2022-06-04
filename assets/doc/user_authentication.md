# User Authentication

Give the user the possibility to sing up, log in and out.

## Templates

1. create a templates/registration :

```powershell
 New-Item -Path ".\templates" -Name "registration"-ItemType "directory"
```

2. Tell Django where to send the users when he logs in and out. Use the **LOGIN_REDIRECT_URL** and **LOGOUT_REDIRECT_URL** settings to do that.

```python
# ... django_project/settings.py
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"
```

- we need to name the homepage URL later 'home'

### create the four necessary templates :

1. **base.html** :  
   The part with _{% block content %}_ will be replaced by the other templates/htmls.

```html
<!-- ... templates/base.html -->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>{% block title %}Restaurant Manager{% endblock title %}</title>
  </head>
  <body>
    <main>{% block content %} {% endblock content %}</main>
  </body>
</html>
```

2. **home.html**  
   Is the home page (_landing page_).

```html
<!-- ... templates/home.html -->
{% extends "base.html" %} {% block title %}Home{% endblock title %} {% block
content %} {% if user.is_authenticated %} Hi {{ user.username }}!
<p><a href="{% url 'logout' %}">Log Out</a></p>
{% else %}
<p>You are not logged in</p>
<a href="{% url 'login' %}">Log In</a> |
<a href="{% url 'signup' %}">Sign Up</a>
{% endif %} {% endblock content %}
```

3. **login.html**
   The Page the user see when he wants to log in (_login form_).

```html
<!-- ... templates/registration/login.html -->
{% extends "base.html" %} {% block title %}Log In{% endblock title %} {% block
content %}
<h2>Log In</h2>
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Log In</button>
</form>
{% endblock content %}
```

4. **signup.html**
   The Page the user see when he wants to sign up (_signup form_).

```html
<!-- ... templates/registration/signup.html -->
{% extends "base.html" %} {% block title %}Sign Up{% endblock title %} {% block
content %}
<h2>Sign Up</h2>
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Sign Up</button>
</form>
{% endblock content %}
```

## URLs

Link to the pages.

1. update django_project/urls.py :

```python
# ... django_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"),
      name="home"),
]
```

- _for now we use the shortcut of importing TemplateView and setting the template_name right in our url pattern._

2. create accounts/urls.py and update it :

```python
# ... accounts/urls.py
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
```

## Views

Logic to connect user actions with views and model.

1. update accounts/views.py :

```python
# ... accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
```

- _contains the logic for our sign up form_
- _We’re using Django’s generic CreateView here and telling it to use our CustomUserCreationForm, to redirect to login once a user signs up successfully, and that our template is named signup.html._
