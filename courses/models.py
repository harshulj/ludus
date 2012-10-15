from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60)
