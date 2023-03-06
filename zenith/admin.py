from django.contrib import admin
from .models import Student, Message, PaymentFile, Payment, dp

# Register your models here.

admin.site.register(Student)
admin.site.register(Message)
admin.site.register(dp)
admin.site.register(Payment)
admin.site.register(PaymentFile)
