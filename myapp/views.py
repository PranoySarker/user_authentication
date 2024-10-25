from django.shortcuts import render
from .models import *

# Create your views here.


#view for register page
def RegisterPage(request):
    return render(request, "app/register.html" )

#view for user registration
def UserRegister(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        #first we will validate user exist or not
        user = User.objects.filter(Email=email)

        if user:
            message = "User already exist"
            return render(request,"app/login.html", {'msg':message})
        else:
            #if user does not exist check confirm password
            if password == cpassword:
                #create the user
                newuser = User.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)
                message = "User register successfully"
                return render(request,"app/login.html", {'msg':message})
            else:
                message = "Password and Confirm Password does not match"
                return render(request,"app/register.html", {'msg':message})

#Login view
def LoginPage(request):
    return render(request, "app/login.html")

# Login User
def LoginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        #checking the email with database
        user = User.objects.get(Email=email)

        if user:
            if user.Password == password:
                #if user matched set data in the session
                request.session['Firstname'] = user.Firstname
                request.session['Lastname'] = user.Lastname
                request.session['Email'] = user.Email
                return render(request, "app/home.html")
            else:
                message = "Password does not match"
                return render(request,"app/login.html",{'msg':message})
        else:
           message = "User does not exist" 
           return render(request, "app/register.html", {'msg':message})
        
