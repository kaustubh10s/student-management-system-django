from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'student_number',
            'first_name',
            'last_name',
            'email',
            'field_of_study',
            'gpa'
        ]

        labels = {
            'student_number': 'Student Number',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'field_of_study': 'Field of study',
            'gpa': 'GPA'
        }

        widgets = {
            'student_number': forms.NumberInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'email': forms.EmailInput(),
            'field_of_study': forms.TextInput(),
            'gpa': forms.NumberInput()
        }


