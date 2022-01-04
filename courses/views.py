from django.shortcuts import render,get_object_or_404, redirect
from .models import Courses
from .forms import CommentForm
from marketing.models import Signup

# Create your views here.
def index(request):
    if request.method == "POST":
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
    return render(request, 'index.html')

def courses(request):
    return render(request, 'courses.html')


def English(request):
    course_list = Courses.objects.filter(categories__title = 'English')
    
    context = {
        'course_list': course_list        
    }
    return render(request, 'english.html', context)

def Math(request):
    course_list = Courses.objects.filter(categories__title = 'Math')
    
    context = {
        'course_list': course_list        
    }
    return render(request, 'math.html', context)

def Geography(request):
    course_list = Courses.objects.filter(categories__title = 'Geography')
    
    context = {
        'course_list': course_list        
    }
    return render(request, 'geography.html', context)

def Biology(request):
    course_list = Courses.objects.filter(categories__title = 'Biology')
    
    context = {
        'course_list': course_list        
    }
    return render(request, 'biology.html', context)

def Chemistry(request):
    course_list = Courses.objects.filter(categories__title = 'chemistry')
    
    context = {
        'course_list': course_list        
    }
    return render(request, 'chemistry.html', context)
 
def course_detail(request, course_id):
     course = get_object_or_404(Courses, id=course_id)
     form = CommentForm(request.POST or None)
     if request.method == 'POST':
         if form.is_valid():
             form.instance.user = request.user
             form.instance.course = course
             
             form.save()
             return redirect('course_detail', course_id = course_id)
     context = {
         'course': course,
         'form':form
     }
     return render(request, 'course_detail.html', context)
 
 
def contact(request):
    return render(request, 'contact.html')
