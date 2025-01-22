from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from django.urls import reverse


def contactPage(request): 
    if request.method == "POST":
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            currContact=contactMessage(name=name, email=email, subject=subject, message=message)
            currContact.save()

            messages.success(request, "Your message has been succesfully sent!")
        
        except Exception as e:
            messages.error(request, f"Error: {e}")

        return redirect(reverse("contact"))
        
    return render(request, "contact.html")
