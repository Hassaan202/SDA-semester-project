from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from django.urls import reverse



# for testing only
def test(request):
    return render(request, "test.html")



#the login function name should be different from the main function name
def login1(request):
    #note that the query string retrieved as part of the GET method, can get using POST via form hidden field 
    next_URL=request.GET.get('next', reverse('home')) #second parameter is the default value if key not found

    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username entered!")
            #this reverse method is very useful as allows for flexibility in case decide to change the urls in the future, it will accomodate evrything with minimal changes
            return redirect(f"{reverse('login')}?next={next_URL}")
        
        user=authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect(f'{reverse("login")}?next={next_URL}')
        
        else:
            login(request, user) #creates a session associated with the user
            return redirect(next_URL)
    
    return render(request, "login.html")



def signup(request):
    #note that pressing the submit button on the form will invoke the same URL but with POST method so this IF condition will be satisfied
    next_URL=request.GET.get('next', reverse('home'))

    if request.method == 'POST':
        #retrieve values from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.info(request, "Username already taken!")
            return redirect(f"{reverse('signup')}?next={next_URL}")
        
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )
        
        user.set_password(password) #password needs to be set seperately as requires hashing
        user.save()
        
        #after registering an account, will have to login again to access the home page
        messages.info(request, "Account created Successfully!")
        return redirect(f"{reverse('login')}?next={next_URL}")
    
    # Render signup page(GET)
    return render(request, 'signup.html')



#logging out the user from the system and redirecting to the login page
def logout1(request):
    logout(request)
    return redirect(reverse('login'))



#index/main page
def home(request):
    return render(request, "index.html")



#profile manager
@login_required
def profileManage(request):
    if request.method=='POST':
        user=request.user

        first_name = request.POST.get('first_name').strip()
        last_name = request.POST.get('last_name').strip()

        old_first_name = request.POST.get('old_first_name')
        old_last_name = request.POST.get('old_last_name')
        
        #if no changes made, don't save to the model
        if (first_name == old_first_name) and (last_name == old_last_name):
            messages.info(request, "No changes made!")
            return redirect(reverse('profile'))
         
        user.first_name=first_name
        user.last_name=last_name
        user.save()

        messages.success(request, "Profile updated succesfully!")
        return redirect(reverse('profile'))

    return render(request, "profile.html")



# def startUpRedirect(request):
#     return redirect(reverse('home'))

