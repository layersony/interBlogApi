# Generated by Django 3.2.9 on 2021-11-06 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0003_alter_tags_tagname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='tagname',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Tag Name'),
        ),
    ]
