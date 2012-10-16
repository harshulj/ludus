from django.shortcuts import render_to_response
from courses.models import Course, ClassTime
from django.template.loader import get_template
from django.template import Context

def courses(request):
    courses = Course.objects.all()
    return render_to_response('courses.html', {'courses': courses})

def schedule(request, course_id=-1):
    if course_id == -1:
        timings = ClassTime.objects.all().order_by('day', 'start_time')
    else:
        timings = ClassTime.objects.filter(course=course_id)
    return render_to_response('schedule.html', {'timings' : timings})
