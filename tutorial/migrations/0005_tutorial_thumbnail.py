# Generated by Django 3.1.4 on 2020-12-15 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0004_auto_20201213_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='thumbnail',
            field=models.ImageField(default='uploads/images/no-img.jpg', upload_to='uploads/'),
        ),
    ]