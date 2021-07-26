# settings
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
    },
    # "postgres": {}
}


# ENGINE - зашиты внуттри django
# django.db.backends.sqlite3


# os.environ - to use for protecting data
# psql --host=localhost --port=5000 --username=postgres postgres
# create user myuser encrypted password 'password'
# create database mydatabase owner myuser; - acess for all roles
# grant all on database mydatabase to myuser ; - all accesses for the user

# start app my app

# Create your models here
# select * from ...
# using ORM instead

# ORM - позволяет работать с базой данных через язык связь бд и пайтон
# class MyModel(models.Model):

# %psql --host=localhost --port=5000 --username=myuser mydatabase
# \dt - to check tables

# дата миграции - для удаления данных в таблицу / изменения / добавления
# you have anaplied migrations

# для того чтоб база данных была в соответсвующем виду в manage .py
# есть две комманды
# migrate
# makemigrations - создает миграции
# showmigrations - показывает миграции
# миграции можно созлавать самостоятельно

# migrate
# showmigrations
# x-показывает статус миграции

# /dt - создано несколько таблиц

# srttings.py + добавляем нашу таблицу

# migrate

# makemigrations --name foo

# \d my_app
# migrate

# Default nextval('myapp_person_id_seq'::reqclass)
# \q


# ---------------------------
# django admin

# permissions of users = AUTH_PASSWORD_VALIDATORS
# не может быть таким же как и логин
# лолжен иметь минимальную длинну

# manage.py create superuser
# создание пользователя

# from django.conf import settings
from django.conf import settings

# urlpatterns = []
# if settings.DEBUG:
#     urlpatterns += [
#         path('/admin', admin.site.urls)
#     ]

# мноие ко многим - авторы и книги
# один ко многим - настройки
