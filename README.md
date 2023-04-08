# login-vuejs-django-ninja

Sistema de Login entre VueJS e Django-Ninja

## Frontend

* Template: [Windmill](https://windmillui.com/dashboard-html)
* Github: [windmill-dashboard](https://github.com/estevanmaito/windmill-dashboard)

### Criando o projeto

```
npm install -g @vue/cli

vue create frontend
cd frontend
yarn dev  # ou
# npm run serve
```


## Backend

### Bibliotecas

* [django-ninja](https://django-ninja.rest-framework.com/)
* [django-ninja-auth](https://github.com/mugartec/django-ninja-auth)
* [django-ninja-jwt](https://eadwincode.github.io/django-ninja-jwt/)

### Criando o projeto

```
python -m venv .venv

source ./venv/bin/activate  # ou
# .venv\Scripts\activate  # Windows

pip install django-ninja-auth

django-admin startproject backend .
cd backend/
python ../manage.py startapp core
```

### Autenticação

[mugartec/django-ninja-auth](https://github.com/mugartec/django-ninja-auth)

TODO: [django-ninja-jwt](https://eadwincode.github.io/django-ninja-jwt/)


### Rotas

Edite `backend/urls.py`

```python
# urls.py
from django.contrib import admin
from django.urls import path

from .api import api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', api.urls),
]
```

Crie e edite `backend/api.py`

```python
# api.py
from ninja import NinjaAPI
from ninja_auth.api import router as auth_router

api = NinjaAPI(csrf=True)

api.add_router('/auth/', auth_router)
```

Acesse a doc em `/api/v1/docs/`

![](img/docs.png)