# models
from django.shortcuts import render, redirect
from .models import StudentModel, CourseModel, EnrollmentModel, InstructorModel, PaymentModel
from .forms import StudentForm, CourseForm, EnrollmentForm, InstructorForm, PaymentForm

# authentication
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm

# models
# def student(request):
#     form = StudentModel.objects.all()
#     return render(request, 'models/student.html', {'form': form})

# def course(request):
#     form = CourseModel.objects.all()
#     return render(request, 'models/course.html', {'form': form})

# def enrollment(request):
#     form = EnrollmentModel.objects.all()
#     return render(request, 'models/enrollment.html', {'form': form})

# def instructor(request):
#     form = InstructorModel.objects.all()
#     return render(request, 'models/instructor.html', {'form': form})

# def payment(request):
#     form = PaymentModel.objects.all()
#     return render(request, 'models/payment.html', {'form': form})

# authentication
def registerUser(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('loginUser')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def loginUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid input.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logoutUser(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('loginUser')

@login_required(login_url='loginUser')
def dashboard(request):
    return render(request, 'base/base.html')

# success
def success(request):
    return render(request, 'base/success.html')

# model form
@login_required(login_url='loginUser')
def studentViews(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StudentForm()
    
    students = StudentModel.objects.all()
    return render(request, 'models/student.html', {
        'form': form,
        'students': students
    })

@login_required(login_url='loginUser')
def courseViews(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CourseForm()
    courses = CourseModel.objects.all()
    return render(request, 'models/course.html', 
                  {'form': form, 
                   'courses': courses})

@login_required(login_url='loginUser')
def enrollmentViews(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = EnrollmentForm()
    enrollment = EnrollmentModel.objects.all()
    return render(request, 'models/enrollment.html', 
                  {'form': form, 
                   'enrollment': enrollment})

@login_required(login_url='loginUser')
def instructorViews(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = InstructorForm()
    instructor = InstructorModel.objects.all()
    return render(request, 'models/instructor.html', 
                  {'form': form, 
                   'instructor': instructor})

@login_required(login_url='loginUser')
def paymentViews(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PaymentForm()
    payment = PaymentModel.objects.all()
    return render(request, 'models/payment.html', 
                  {'form': form, 
                   'payment': payment})