from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    verified=models.BooleanField(default=False)
    hostel_address=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    school=models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    lecture_theatre=models.CharField(max_length=100)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Student: {self.owner}. Verified: {self.verified}"

class dp(models.Model):
    display_picture = models.ImageField(upload_to='images/', blank=True, null=True)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Dp of {self.owner}"

class Payment(models.Model):
    full_name= models.CharField(max_length=100)
    email= models.EmailField()
    owner=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Payment details of {self.owner}"

class PaymentFile(models.Model):
    payment_file=models.FileField()
    owner=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Payment File of {self.owner}"

class Message(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    owner=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Message from {self.owner}"

class Image(models.Model):
    about_us_image=models.ImageField(upload_to='images/', blank=True, null=True)
