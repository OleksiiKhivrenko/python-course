from django.db import models


class JobTitle(models.Model):
    job.title = models.CharField(max_length=32)

# Create your models here.
class Person(models.Model):
    """Person model implementation
    Будет отображаться в бд myapp_person"""

    # primary_key = models.AutoField(primary_key=True)
    """primary_key - создание ключа вручную"""

    slug = models.SlugField(verbose_name="slug")
    """строка, длина не ограничена не более 255 символов, 
    может содержать буквы латинского алфавита в нижнем и 
    верхнем регистре цифры и _ 
    verbose_name - имя поля но человеко читаемое"""

    first_name = models.CharField(max_length=255, verbose_name="a person's first name")
    """char field - 1 параметр который ограничивает длинну
    null - для отображения в которых ничего нет используется null 
    null=False - не может содержать null
    если не передаете - автоматом ставится null
    blank=True - поле может быть пустым
    default='slug'  default='default'
    unique=True - могут ли быть коллизии на уровне таблицы
    null=False, blank=False, default=None, unique=False - default
    max_length - обязательный для CharField
    verbose_name = a person's first name"""

    last_name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    """может быть расширен на уровне валидаций"""

    sex = models.BooleanField()
    """default True/False"""

    salary = models.DecimalField(verbose_name="a salary size per month", decimal_places=2, max_digits=10,
                                 default=1000.0)
    """Decimal позволяет хранить не целчисленные числа
    max_digits=10 decimal_places=2 default=1000.0"""

    # job_title = models.ForeignKey(JobTitle, on_delete=)
    # models.DO_NOTHING
    # models.CASCADE - все запси и све свзяи
    # models.PROTECTED - защита от удаления
    # models.SET_NULL - проставятся null все связи
    # models.SET_DEFAULT - установятся все связи в default

    # doc django.com/ search by fields

    def __str__(self):
        """Return a string version of an instance"""
        return f"{self.first_name} {self.last_name}"
