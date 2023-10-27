from django.db import models
from django.contrib.auth.models import User 
from django.shortcuts import reverse
from app.utils import GenericComments

# Create your models here.

class Articles(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    newswriter = models.ForeignKey(to=User, on_delete=models.SET_NULL, editable=False,null=True)
    some = models.CharField(blank=True, null=True, max_length=22)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('article', kwargs = {'id':self.id})
    
    def get_comment():
        return ArticleComment


class ArticleComment(GenericComments):
    article = models.ForeignKey('Articles', on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(auto_now_add=True)
