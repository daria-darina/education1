from django.urls import path

from . import views
from django.views.generic import RedirectView
from .views import (

    TestView,
    LogoutView,
    CoursesView,
    DetailView,
    CourseByUserListView,
    LessonView,
    CourseWorkView,

    add_to_course,
)


app_name = 'app'
urlpatterns = [
    path('', CoursesView.as_view(), name='courses'),
    path('details/<int:pk>/', DetailView.as_view(), name='details'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('article/', TestView.as_view(), name='article'),
    path('coursework/', CourseWorkView.as_view(), name='coursework'),
    path('my_courses/', CourseByUserListView.as_view(), name='my_courses'),
    path('lesson/', LessonView.as_view(), name='lesson'),


    path('add-to-course/<int:pk>/', add_to_course, name='add-to-course'),
]
