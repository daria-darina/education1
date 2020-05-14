from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.views import View, generic

from .models import DescriptionCourse


# Create your views here.
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('app:courses')

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
                    return render(request, 'central/courses.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'central/login.html', {'form': form})

from docxtpl import DocxTemplate


class TestView(View):

    def get(self, request):
        return render(request, 'central/article.html')

    def post(self, request):
        title = request.POST['title']
        name = request.POST['name']
        university = request.POST['university']
        address = request.POST['address']
        email = request.POST['email']
        annotation = request.POST['annotation']
        introduction = request.POST['introduction']
        article = request.POST['article']
        conclusion = request.POST['conclusion']
        literature = request.POST['literature']

        document = DocxTemplate('example.docx')
        context = {'title': title, 'name': name, 'university': university, 'address': address, 'email': email,
                   'annotation': annotation, 'introduction': introduction, 'article': article, 'conclusion': conclusion,
                   'literature': literature}
        document.render(context)
        # document.save("generated_doc.docx")

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename=download.docx'
        document.save(response)

        return response


from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Course


class CourseByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = Course
    template_name = 'central/my_courses.html'
    paginate_by = 10

    def get_queryset(self):
        return Course.objects.filter(student=self.request.user)