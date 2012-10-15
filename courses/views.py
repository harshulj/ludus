from django.http import HttpResponse
from courses.models import Course
from django.template.loader import get_template
from django.template import Context

def courses(request):
    courses = Course.objects.all()
    t = get_template('courses.html')
    html = t.render(Context({'courses': courses}))
    return HttpResponse(html)
