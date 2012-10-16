from courses.models import *
from django.contrib import admin

class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'slug']

class FacultyAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'slug']

class ClassTimeAdmin(admin.ModelAdmin):
    list_display = ['course', 'day', 'start_time', 'end_time']

admin.site.register(ClassTime, ClassTimeAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Course, CourseAdmin)
