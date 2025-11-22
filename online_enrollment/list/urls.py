from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.studentViews, name='student'),
    path('course/', views.courseViews, name='course'),
    path('enrollment/', views.enrollmentViews, name='enrollment'),
    path('instructor/', views.instructorViews, name='instructor'),
    path('payment/', views.paymentViews, name='payment'),
    path('success/', views.success, name='success'),

    path('', views.loginUser, name='loginUser'),
    path('logoutUser/', views.logoutUser, name='logoutUser'),
    path('registerUser/', views.registerUser, name='registerUser'),
    path('dashboard/', views.dashboard, name='dashboard'),
]