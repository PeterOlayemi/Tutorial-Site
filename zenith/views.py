from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from .forms import RegisterForm, StudentRegisterForm,MessageForm, DpForm, PaymentForm, PaymentFileForm
from .models import Student, dp
# Create your views here.

def home(request):
    return render(request, 'zenith/home.html')

@login_required
def message(request):
    if request.method != 'POST':
        form = MessageForm()
    else:
        # Process completed form.
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.owner=request.user
            message.save()
            return HttpResponseRedirect(reverse('zenith:home'))
    context = {'form': form}
    return render(request, 'zenith/message.html', context)

@login_required
def paymentfile(request):
    if request.method != 'POST':
        form = PaymentFileForm()
    else:
        # Process completed form.
        form = PaymentFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.owner=request.user
            file.save()
            return HttpResponseRedirect(reverse('zenith:paymentdetail'))
    context = {'form': form}
    return render(request, 'zenith/paymentfile.html', context)

@login_required
def paymentdetail(request):
    if request.method != 'POST':
        form = PaymentForm()
    else:
        # Process completed form.
        form = PaymentForm(request.POST)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.owner=request.user
            detail.save()
            return HttpResponseRedirect(reverse('zenith:paymenthome'))
    context = {'form': form}
    return render(request, 'zenith/paymentdetail.html', context)

@login_required
def payment(request):
    return render(request, 'zenith/payment.html')

@login_required
def viewprofile(request):
    data=Student.objects.filter(owner=request.user)
    hotel=dp.objects.filter(owner=request.user)
    context={'data':data, 'hotel':hotel}
    return render(request, 'zenith/studentprofile.html', context)

@login_required
def editprofile(request, _id):
    data=Student.objects.get(id=_id)
    if request.method != 'POST':
        form = StudentRegisterForm(instance=data)
    else:
        form = StudentRegisterForm(instance=data, data=request.POST)
        if form.is_valid():
            new_profile=form.save(commit=False)
            new_profile.owner=request.user
            new_profile.save()
            return HttpResponseRedirect(reverse('zenith:studentprofile'))
    context = {'data': data, 'form': form}
    return render(request, 'zenith/editprofile.html', context)

@login_required
def editdp(request, _id):
    data=dp.objects.get(id=_id)
    if request.method != 'POST':
        form = DpForm(instance=data)
    else:
        form = DpForm(request.POST, request.FILES)
        if form.is_valid():
            data.delete()
            new_dp=form.save(commit=False)
            new_dp.owner=request.user
            new_dp.save()
            return HttpResponseRedirect(reverse('zenith:studentprofile'))
    context = {'data': data, 'form': form}
    return render(request, 'zenith/editdp.html', context)

@login_required
def studentregister(request):
    if request.method != 'POST':
        form = StudentRegisterForm()
    else:
        # Process completed form.
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            new_student = form.save(commit=False)
            new_student.owner=request.user
            new_student.save()
            return HttpResponseRedirect(reverse('zenith:home'))
    context = {'form': form}
    return render(request, 'zenith/studentregister.html', context)

@login_required
def hotel_image_view(request):
  
    if request.method == 'POST':
        form = DpForm(request.POST, request.FILES)
  
        if form.is_valid():
            display=form.save(commit=False)
            display.owner=request.user
            display.save()
            return HttpResponseRedirect(reverse('zenith:studentregister'))
    else:
        form = DpForm()
    return render(request, 'zenith/imageform.html', {'form' : form})

@login_required
def aboutus(request):
    return render(request, 'zenith/aboutus.html')

@login_required
def contactus(request):
    return render(request, 'zenith/contactus.html')

def signup(request):
    if request.method != 'POST':
        form = RegisterForm()
    else:
        # Process completed form.
        form = RegisterForm(data=request.POST)
 
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('zenith:image_upload'))

    context = {'form': form}
    return render(request, 'zenith/signup.html', context)

@login_required
def signout(request):
    logout(request)
    return redirect('zenith:home')
