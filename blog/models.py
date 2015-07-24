from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 128, unique = True)

    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length = 128)
    body = models.TextField()
    url = models.URLField()
    views = models.IntegerField(default = 0)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title


# Create your models here.
