from django.contrib import admin
from .models import StudentModel, CourseModel, EnrollmentModel, InstructorModel, PaymentModel

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('studentId', 'name', 'phoneNo', 'address', 'enrollmentYr') 

@admin.register(CourseModel)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('courseID', 'courseCode', 'prequisite', 'schedule', 'maxStudents') 

@admin.register(EnrollmentModel)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('enrollmentID', 'studentID', 'courseID', 'enrollmentDL', 'grade') 

@admin.register(InstructorModel)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('instructorID', 'position', 'courseTeaching', 'hiredDate', 'officeLocation') 

@admin.register(PaymentModel)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('paymentID', 'studentID', 'transactID', 'paymentStatus') 