# Graph models

Renders a graphical overview of your project models and apps as an png.  
_See [youtube link](https://www.youtube.com/watch?v=yvf_J225iM8) for tutorial._

## setup

1. install [**django-extensions**](https://pypi.org/project/django-extensions/) :

```powershell
python -m pip install django-extensions
```

- add the app to the installed app setting :

```python
# ... django_project/settings.py
INSTALLED_APPS = [
    # ...
    'django_extensions',
]
```

2. install [**Graphviz**](http://www.graphviz.org/) _(choose 'add to path' when installing and restart terminal)_ if not already installed on operating system.

3. add the [**Graph models**](https://django-extensions.readthedocs.io/en/latest/graph_models.html) library :

```powershell
python -m pip install pyparsing pydot
```

## command to create png

- create a graph from all models

```powershell
py manage.py graph_models -a -o my_project_visualized.png
```

- create a graph for only certain models (**-I Foo,Bar**) in this example for Foo and Bar

```powershell
py manage.py graph_models -a -I Foo,Bar -o my_project_subsystem.png
```

- the same as above but with arrow shaped arrows (**--arrow-shape normal**) and application grouping (**-g**)

```powershell
py manage.py graph_models -a -g -I Post,User --arrow-shape normal -o my_project_sans_foo_bar.png
```
