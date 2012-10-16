from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=10, unique='true')
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60)

    def __unicode__(self):
        return self.name


class Faculty(models.Model):
    salutation = models.CharField(max_length=4, default='Dr')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    code = models.CharField(max_length=5, unique='true')
    slug = models.SlugField(max_length=50)
    courses = models.ManyToManyField(Course, related_name='faculties')

    class Meta():
        verbose_name_plural = "faculties"

    @property
    def name(self):
        return self.salutation + '. ' + self.first_name + ' ' + self.last_name

    def __unicode__(self):
        return self.name

class ClassTime(models.Model):
    DAY_CHOICES = (
        ('0', 'Sunday'),
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        )
    course = models.ForeignKey(Course)
    day = models.CharField(max_length=1, choices=DAY_CHOICES, default=1)
    start_time = models.TimeField()
    end_time = models.TimeField()
