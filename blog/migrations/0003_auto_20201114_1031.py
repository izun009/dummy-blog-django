# Generated by Django 3.1.3 on 2020-11-14 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201114_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, editable=False),
        ),
    ]
