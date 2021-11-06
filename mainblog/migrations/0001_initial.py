# Generated by Django 3.2.9 on 2021-11-06 03:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('baseblog_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mainblog.baseblog')),
                ('tagname', models.CharField(blank=True, max_length=150, null=True, verbose_name='Tag Name')),
            ],
            bases=('mainblog.baseblog',),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('baseblog_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mainblog.baseblog')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('blogDetail', models.TextField(verbose_name='Blog')),
                ('category', models.CharField(max_length=200, verbose_name='Category')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='mainblog.Tags')),
            ],
            options={
                'ordering': ['-id'],
            },
            bases=('mainblog.baseblog',),
        ),
    ]