from django.db import models
from django.contrib.auth.models import User

class BaseBlog(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

class Tags(BaseBlog):
  tagname = models.CharField('Tag Name', max_length=150, null=True, blank=True)

  def __str__(self):
      return self.tagname

class Blog(BaseBlog):
  title = models.CharField('Title', max_length=150, null=False, blank=False)
  blogDetail = models.TextField('Blog', null=False, blank=False)
  category = models.CharField('Category', max_length=200, null=False, blank=False)
  tags = models.ManyToManyField(Tags, blank=False)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title

  class Meta:
    ordering = ['-id']