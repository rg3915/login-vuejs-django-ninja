# login-vuejs-django-ninja

Sistema de Login entre VueJS e Django-Ninja

## Frontend

* Template: [Windmill](https://windmillui.com/dashboard-html)
* Github: [windmill-dashboard](https://github.com/estevanmaito/windmill-dashboard)

### Instalação

```
npm install -g @vue/cli
```

#### Use [node](https://nodejs.org/en/) com [nvm](https://github.com/nvm-sh/nvm).

```
nvm use 18.3.0
```


### Criando o projeto

```
vue create frontend

vue add router

cd frontend
yarn dev  # ou
# npm run serve
```

Ref: [alpinejs-tailwindcss-example](https://github.com/rg3915/alpinejs-tailwindcss-example)

![](https://camo.githubusercontent.com/433b9e46931996dab58a0231b202aad43e24ce6bd7c7f04c1e32fb88b1b43b61/68747470733a2f2f77696e646d696c6c75692e636f6d2f696d672f44617368626f6172642e706e67)

### Instalando TailwindCSS

[Leia mais](install_tailwind.md)


## Dados com [json-server](https://www.npmjs.com/package/json-server) (Opcional)

```
npm i -g json-server
```

Crie `db.json`

```
touch db.json
```

```json
{
  "todos": [
    {
      "id": 1,
      "task": "One"
    },
    {
      "id": 2,
      "task": "Two"
    },
    {
      "id": 3,
      "task": "Three"
    }
  ]
}
```

Rode o json-server

```
json-server --watch db.json
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