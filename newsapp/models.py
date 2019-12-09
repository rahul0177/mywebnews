from django.db import models

# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=300)
    news=models.CharField(max_length=1000)
    category=models.CharField(max_length=40)
    published=models.CharField(max_length=40,default="")
    author=models.CharField(max_length=20,default="")
    url=models.CharField(max_length=100,default="")

    def __str__(self):
        return self.category

class Headnews(models.Model):
    title=models.CharField(max_length=300)
    news=models.CharField(max_length=1000)
    images=models.ImageField()

    def __str__(self):
        return self.title

