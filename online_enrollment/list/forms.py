from django import forms
from .models import StudentModel, CourseModel, EnrollmentModel, InstructorModel, PaymentModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # REMOVING HELP TEXT BECAUSE IT'S SO FKING ANNOYING
        for field_name in ['password1', 'password2', 'username']:
            self.fields[field_name].help_text = None

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = '__all__'

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = EnrollmentModel
        fields = '__all__'

class InstructorForm(forms.ModelForm):
    class Meta:
        model = InstructorModel
        fields = '__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentModel
        fields = '__all__'