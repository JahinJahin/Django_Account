
from django.forms import Form
from django.http import HttpResponse
from django.shortcuts import redirect, render
from medicine.forms import MedicineForm
from medicine.models import medicine
from django.contrib.auth.forms import UserCreationForm,User
from django.contrib.auth.decorators import login_required
from medicine.forms import signupform
from django.contrib import messages

# Create your views here.
def index(request):
    if 'p' in request.GET:
        p=request.GET['p']
        obj=medicine.objects.filter(name=p)
    else:
        obj = medicine.objects.all()
    return render(request,'index.html',{'data':obj})

    return render(request,"index.html")

def delete(request,id):
    obj = medicine.objects.get(id=id)
    obj.delete()
 
    return redirect ('home')
    return render(request,"delete.html",{'data':obj})

def base(request):
    return render(request,"base.html")
   
def add(request):
    if request.method == "POST":
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
            
    else:
        form = MedicineForm
        context = {
           'form' : form
        }
    return render(request,"add.html",context)

def search(request):
    return render(request,"search.html")

def edit(request,id):
    obj =medicine.objects.get(id=id)
    form=MedicineForm(instance=obj)
    if request.method == "POST":
        form = MedicineForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("home")
            
    
    context = {
           'form' : form
        }

    return render(request,"edit.html",context)


def register(request):
  
    if request.method  == "POST":
       name =request.POST["username"]
       email =request.POST["email"]
       password1=request.POST["password1"]
       password2 =request.POST["password2"]
       if password1 == password2: 
          user=User.objects.create_user(username=name,email=email,password=password1)
          user.is_staff=True
          user.save()
          return redirect('login')
       else:
     
           return redirect('register')
    else:
        form=signupform()
    return render (request,'registration/register.html',{'form' : form})

def profile (request):
    return render(request,'profile.html')

