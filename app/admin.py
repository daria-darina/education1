from django.contrib import admin
from .models import Lesson
from .models import Course
from .models import DescriptionCourse
#from .models import CourseUser

# Register your models here.


admin.site.register(Lesson)
#admin.site.register(CourseUser)
admin.site.register(Course)
admin.site.register(DescriptionCourse)