from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.views import View
from .models import DescriptionCourse


# Create your views here.
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('central:courses')




class CoursesView(View):
    def get(self, request):
        events = DescriptionCourse.objects.all()
        return render(request, 'central/courses.html', {'events': events})

class DetailView(View):
    def get(self, request, *args, **kwargs):
        details = get_object_or_404(DescriptionCourse, pk=kwargs['pk'])
        context = {'details': details}
        return render(request, 'central/details.html', context)

from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'central/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'central/register.html', {'user_form': user_form})

from django.http import HttpResponse
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'central/login.html', {'form': form})