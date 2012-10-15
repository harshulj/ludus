from django.shortcuts import render_to_response
from courses.models import Course
from django.template.loader import get_template
from django.template import Context

def courses(request):
    courses = Course.objects.all()
    return render_to_response('courses.html', {'courses': courses})
