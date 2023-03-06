from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Student, Message, dp, Payment, PaymentFile


class RegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=30, required=True, help_text='Enter your First Name')
    last_name=forms.CharField(max_length=30, required=True, help_text='Enter Your Last Name')
    email=forms.EmailField(max_length=50, help_text='Enter a valid email address')

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

class StudentRegisterForm(forms.ModelForm):
    date_of_birth=forms.DateField(required=True, help_text='Enter Your Date of Birth in (yyyy-mm-dd)')
    school=forms.CharField(required=True, help_text='Enter the Full Name of your Institution of Learning')
    phone_number = forms.CharField(required=True, help_text='A WhatsApp Enabled Phone Number is Required')
    hostel_address = forms.CharField(required=True, help_text='Enter your Hostel Address in Full')
    level = forms.CharField(required=True, help_text='Enter Your Level')
    department=forms.CharField(required=True, help_text='Enter Your Department')
    lecture_theatre=forms.CharField(required=True, help_text='Enter the Name of the Lecture Theatre Where You Receive Most Lectures')

    class Meta:
        model = Student
        fields=['date_of_birth','school','phone_number','hostel_address','level','department','lecture_theatre']
        labels={}

class DpForm(forms.ModelForm):
    display_picture=forms.ImageField(required=True, help_text='Add a Clear Image of You')

    class Meta:
        model = dp
        fields = ['display_picture']

class MessageForm(forms.ModelForm):
    full_name=forms.CharField(required=True, help_text='Enter Your Full Name')
    email=forms.EmailField(required=True, help_text='Enter Your Email To Receive Response From Zenith Tutorial')
    message=forms.Textarea()

    class Meta:
        model=Message
        fields=['full_name','email','message']
        labels={}

class PaymentForm(forms.ModelForm):
    full_name=forms.CharField(required=True, help_text='Enter Your Full Name')
    email=forms.EmailField(required=True, help_text='Enter Your Email To Receive Payment Updates From Zenith Tutorial')

    class Meta:
        model=Payment
        fields=['full_name','email']
        labels={}

class PaymentFileForm(forms.ModelForm):
    payment_file=forms.FileField(required=True, help_text='Add File of Debit Alert in jpg/png/pdf/doc/docx')

    class Meta:
        model=PaymentFile
        fields=['payment_file']
        labels={}
