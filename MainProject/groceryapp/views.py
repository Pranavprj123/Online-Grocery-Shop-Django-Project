from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .models import *
# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'navigation.html')

def about(request):
    return render(request, 'about.html')

def main(request):
    data = Carousel.objects.all()
    dic = {'data':data}
    return render(request, 'index.html', dic)

def adminLogin(request):
    msg = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        try:
            if user.is_staff:
                login(request, user)
                msg = "User login successfully"
                return redirect('admindashboard')
            else:
                msg = "Invalid Credentials"
        except:
            msg = "Invalid Credentials"
    dic = {'msg': msg}
    return render(request, 'admin_login.html', dic)


def adminHome(request):
    return render(request, 'admin_base.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
