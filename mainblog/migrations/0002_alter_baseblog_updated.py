# Generated by Django 3.2.9 on 2021-11-06 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseblog',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
