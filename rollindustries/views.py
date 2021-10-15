from django.shortcuts import render
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .models import Contact


############################################################
# Main Website Page
############################################################
def homePage(request):
    if request.method == "POST":
        # contact model instance
        contact = Contact()

        # get post values from contact
        toName = request.POST.get("name")
        toEmail = request.POST.get("email")
        phone = request.POST.get("phone")
        emailMessage = request.POST.get("subject")

        # store the value in the database contancts model
        contact.full_name = toName
        contact.email = toEmail
        contact.phone = phone
        contact.subject = emailMessage
        contact.save()

        # Send email to user who contacted the company
        template = render_to_string('rollindustries/email_template.html',
                                    {'name': toName})
        email = EmailMessage(
            'Thank You For Contacting Roll Industries.',
            template,
            settings.EMAIL_HOST_USER,
            [toEmail],
        )
        email.fail_silently = False
        try:
            email.send()
            messages.success("Message Seccessfully Sent!")
        except (Exception):
            messages.error('Unable to Send confirmation email!!')
            pass

    return render(request, 'rollindustries/index.html')


#############################################################
# Oringin Mode View
#############################################################
def originMode(request):
    return render(request, 'rollindustries/origin.html')


def handler400(request, exception=None):
    response = render(request, "rollindustries/400.html", {})
    return response


def handler403(request, exception=None):
    response = render(request, "rollindustries/403.html", {})
    return response


def handler404(request, exception):
    response = render(request, "rollindustries/404.html", {})
    return response


def handler500(request, exeption=None):
    response = render(request, "rollindustries/500.html", {})
    return response
