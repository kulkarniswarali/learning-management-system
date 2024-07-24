from django.shortcuts import render, redirect
from .models import *
from accounts.models import *
from courses.forms import *
# Create your views here.

def index(request):
    courses = Course.objects.all()
    instructors = Profile.objects.filter(category='Instructor')[:3]
    context = {'courses':courses, 'instructors':instructors}
    return render(request, 'courses/main.html', context)


def about(request):
    context = {}
    return render(request, 'courses/about.html', context)

def courses(request):
    courses = Course.objects.all()
    context = {'courses':courses,}
    return render(request, 'courses/courses.html', context)

def courseDetails(request,pk):
    course = Course.objects.get(id=pk)
    myCourse = MyCourse.objects.filter(course=course)
    context = {'course':course, 'mycourse':myCourse}
    return render(request, 'courses/course-details.html', context)

def trainers(request):
    instructors = Profile.objects.filter(category='Instructor')
    context = {'instructors':instructors}
    return render(request, 'courses/trainers.html', context)

def mycourses(request):
    courses = MyCourse.objects.filter(profile=request.user.profile)
    context = {'courses':courses,}
    return render(request, 'courses/mycourses.html', context)

def courseAttempt(request,pk):
    course = MyCourse.objects.get(id=pk)
    topics = course.course.topics.all()
    context = {'course':course, 'topics':topics}
    return render(request, 'courses/course-attempt.html', context)

def checkout(request):
    context = {}
    return render(request, 'courses/checkout.html', context)


def adminPanel(request):
    context = {}
    return render(request, 'courses/admin-panel.html', context)

def users(request):
    u = Profile.objects.all()
    context = {'users':u}
    return render(request, 'courses/users.html', context)

def editusers(request,pk):
    u = Profile.objects.get(id=pk)
    form = ProfileForm(instance=u)
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=u)
        if form.is_valid():
            form.save()
            return redirect('users')  # Redirect to a success page
    else:
        form = ProfileForm()
    context = {'users':u, 'form':form}
    return render(request, 'courses/edit-users.html', context)

def courseMgmt(request):
    context = {}
    return render(request, 'courses/course-mgmt.html', context)

def subscribe(request,pk):
    mycourse = Course.objects.get(id=pk)
    if request.method == 'POST':
        c = MyCourse.objects.create(course=mycourse,profile=request.user.profile, progress=0) 
        return redirect('courseDetails', pk)   
    context = {'course':mycourse}
    return render(request, 'courses/subscribe.html', context)