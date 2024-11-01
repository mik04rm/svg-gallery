from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length=100)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField(default=timezone.now)
    artists = models.ManyToManyField(User, related_name='images')
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title

class Rectangle(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    x = models.IntegerField()
    y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    fill_color = models.CharField(max_length=7, default='#0000FF')
    def __str__(self):
        return f'{self.x} {self.y} {self.width} {self.height}'
    



