from django.db import models
from django.contrib.auth.models import User


class GenericComments(models.Model):
    comment = models.CharField(max_length=255)
    writer = models.ForeignKey(to=User, on_delete=models.SET_NULL, editable=False,null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.pk
    
