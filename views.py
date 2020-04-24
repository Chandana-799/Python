from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def indexView(request):
    return render(request,'index.html')

@login_required
def detailsView(request):
    return render(request,'details.html')

def dashboardView(request):
    return render(request,'Registration/dashboard.html')

def paymentView(request):
    return render(request,'Registration/payment.html')

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})
