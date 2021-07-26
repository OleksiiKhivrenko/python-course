# Generated by Django 3.2.5 on 2021-07-24 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('first_name', models.CharField(max_length=255, verbose_name="a person's first name")),
                ('last_name', models.CharField(max_length=255)),
                ('age', models.IntegerField(default=0)),
                ('sex', models.BooleanField()),
                ('salary', models.DecimalField(decimal_places=2, default=1000.0, max_digits=10, verbose_name='a salary size per month')),
            ],
        ),
    ]