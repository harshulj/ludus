from courses.models import Course
from django.contrib import admin

class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'slug']

admin.site.register(Course, CourseAdmin)
