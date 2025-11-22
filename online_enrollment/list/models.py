from django.db import models

class StudentModel(models.Model):
    studentId = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phoneNo = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    enrollmentYr = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.studentId}'
    
class CourseModel(models.Model):
    courseID = models.CharField(max_length=100)
    courseCode = models.CharField(max_length=100)
    prequisite = models.BooleanField()
    schedule = models.TimeField()
    maxStudents = models.IntegerField()

    def __str__(self):
        return f'{self.courseID}'
    
class EnrollmentModel(models.Model):
    enrollmentID = models.CharField(max_length=100)
    studentID = models.CharField(max_length=100)
    courseID = models.CharField(max_length=100)
    enrollmentDL = models.DateField()
    grade = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.enrollmentID}'
    
class InstructorModel(models.Model):
    instructorID = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    courseTeaching = models.CharField(max_length=100)
    hiredDate = models.DateField()
    officeLocation = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.instructorID}'
    
class PaymentModel(models.Model):
    paymentID = models.CharField(max_length=100)
    studentID = models.CharField(max_length=100)
    transactID = models.CharField(max_length=100)
    paymentStatus = models.BooleanField()

    def __str__(self):
        return f'{self.paymentID}'