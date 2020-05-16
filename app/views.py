from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth import login, authenticate, logout
from django.views import View, generic
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import DescriptionCourse
from .models import Lesson


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

class CourseWorkView(View):

    def get(self, request):
        return render(request, 'central/coursework.html')

    def post(self, request):
        university = request.POST['university']
        institute = request.POST['institute']
        kafedra = request.POST['kafedra']
        way = request.POST['way']
        task = request.POST['task']
        number = request.POST['number']
        group = request.POST['group']
        year = request.POST['year']
        student = request.POST['student']
        degree = request.POST['degree']
        teacher = request.POST['teacher']
        city = request.POST['city']
        introduction = request.POST['introduction']
        body = request.POST['body']
        conclusion = request.POST['conclusion']
        literature = request.POST['literature']

        document = DocxTemplate('курсовая.docx')
        context = {'university': university, 'institute': institute, 'kafedra': kafedra, 'way': way, 'task': task,
                   'number': number, 'group': group, 'year': year, 'student': student, 'degree': degree,
                   'teacher': teacher, 'city': city,'introduction': introduction, 'body': body,
                   'conclusion': conclusion, 'literature': literature}
        document.render(context)
        # document.save("generated_doc.docx")

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename=download.docx'
        document.save(response)

        return response

class DiplomaView(View):

    def get(self, request):
        return render(request, 'central/diploma.html')

    def post(self, request):
        university = request.POST['university']
        institute = request.POST['institute']
        kafedra = request.POST['kafedra']
        way = request.POST['way']
        profile = request.POST['profile']
        task = request.POST['task']
        number = request.POST['number']
        group = request.POST['group']
        year = request.POST['year']
        student = request.POST['student']
        degree = request.POST['degree']
        teacher = request.POST['teacher']
        degree_head = request.POST['degree_head']
        head_teacher = request.POST['head_teacher']
        city = request.POST['city']
        introduction = request.POST['introduction']
        body = request.POST['body']
        conclusion = request.POST['conclusion']
        literature = request.POST['literature']

        document = DocxTemplate('дипломная.docx')
        context = {'university': university, 'institute': institute, 'kafedra': kafedra, 'way': way,
                   'profile': profile, 'task': task, 'number': number, 'group': group, 'year': year,
                   'student': student, 'degree': degree, 'teacher': teacher, 'degree_head': degree_head,
                   'head_teacher': head_teacher,'city': city,'introduction': introduction, 'body': body,
                   'conclusion': conclusion, 'literature': literature}
        document.render(context)
        # document.save("generated_doc.docx")

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename=download.docx'
        document.save(response)

        return response


from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Course

#выводит курсы, на котрые записан польз-ль
class CourseByUserListView(LoginRequiredMixin, generic.ListView):

    model = Course
    template_name = 'central/my_courses.html'
    paginate_by = 10
    context_object_name = 'course_user_list'

    def get_queryset(self):
        return Course.objects.filter(student=self.request.user)

#выводит все уроки курса, на кот:3. щаписан поль-ль
class LessonView(View):
    def get(self, request):
        lessons = Lesson.objects.all()
        lesson_form = LessonForm()
        return render(request, 'central/lesson.html', {'lessons': lessons, 'lesson_form': lesson_form})


def add_to_course(request, pk):
    course = Course.objects.get(pk=pk)
    course.student = request.user
    course.save()
    return HttpResponseRedirect('/')

from .forms import LessonForm


@login_required
@require_http_methods(['POST'])
def Upload_file(request):
    lesson_form = LessonForm(request.POST, request.FILES)
    if lesson_form.is_valid():
        lesson_form.save()

    return HttpResponseRedirect(reverse('app:lesson'))
