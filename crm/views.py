from django.shortcuts import render,redirect
from .forms import Login

# Create your views here.
def register(request):
    return render(request,"crm/register.html")
def Login(request):
    form=Login()
    context={}
    context["form"]=form
    if request.method == "POST":
        form=Login(request.POST)
        if form.is_valid():
            form.save()
            print("user created")
            return redirect("register")
        else:
            context["form"]=form
            return render(request,"crm/Login.html",context)
        return render(request, "crm/Login.html", context)