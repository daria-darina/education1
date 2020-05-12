from django.urls import path

from . import views
from .models import DescriptionCourse
from django.conf.urls.static import static
from django.conf import settings
from .views import (


    LogoutView,
    CoursesView,
    DetailView,
)


app_name = 'app'
urlpatterns = [
    path('', CoursesView.as_view(), name='courses'),
    path('<int:pk>/', DetailView.as_view(), name='details'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
