from django.shortcuts import redirect, render
from django.contrib import messages


from .models import Contact


# Create your views here.


def homePage(request):
    if request.method == "POST":
        # contact model instance
        contact = Contact()

        # get post values from contact
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")

        # store the value in the database model
        contact.full_name = name
        contact.email = email
        contact.phone = phone
        contact.subject = subject
        contact.save()

    return render(request, 'rollindustries/index.html')


def legacyMode(request):
    return render(request, 'rollindustries/origin.html')
