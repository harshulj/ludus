from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60)

    def __unicode__(self):
        return self.name


class Faculty(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    slug = models.SlugField(max_length=50)
    courses = models.ManyToManyField(Course, related_name='faculties')

    @property
    def name(self):
        return self.first_name + ' ' + self.last_name

    def __unicode__(self):
        return self.name
