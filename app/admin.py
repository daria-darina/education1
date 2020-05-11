from django.contrib import admin
from .models import Lesson
from .models import Course
from .models import DescriptionCourse

# Register your models here.


admin.site.register(Lesson)
admin.site.register(Course)
admin.site.register(DescriptionCourse)