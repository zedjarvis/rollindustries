from django.shortcuts import render
from .models import Contact


############################################################
# Main Website Page
############################################################
def homePage(request):
    if request.method == "POST":
        # contact model instance
        contact = Contact()

        # get post values from contact
        fromName = request.POST.get("name")
        fromEmail = request.POST.get("email")
        phone = request.POST.get("phone")
        emailMessage = request.POST.get("subject")

        # store the value in the database model
        contact.full_name = fromName
        contact.email = fromEmail
        contact.phone = phone
        contact.subject = emailMessage
        contact.save()

    return render(request, 'rollindustries/index.html')


#############################################################
# Oringin Mode View
#############################################################
def originMode(request):
    return render(request, 'rollindustries/origin.html')


##############################################################
# Cutom error Page For uniplimented pages
##############################################################
def errorPage(request):
    return render(request, 'rollindustries/error-404.html')
