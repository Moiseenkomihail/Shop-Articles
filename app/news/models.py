from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(blank=True,null=True,upload_to='images/')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    