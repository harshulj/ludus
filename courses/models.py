from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60)

class Faculty(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    slug = models.SlugField(max_length=50)

    @property
    def name(self):
        return self.first_name + ' ' + self.last_name
