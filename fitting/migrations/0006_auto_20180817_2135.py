# Generated by Django 2.0.6 on 2018-08-17 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitting', '0005_module_tier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hull',
            name='name',
            field=models.TextField(max_length=40, unique=True, verbose_name='Hull name'),
        ),
    ]
