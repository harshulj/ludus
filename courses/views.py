# Create your views here.
from django.http import HttpResponse
from courses.models import Course

def courses(request):
    course = Course.objects.get(id=2)
    html = course.name
    return HttpResponse(html)
    
