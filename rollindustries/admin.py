from django.contrib import admin

# Register your models here.
from rollindustries.models import Contact


admin.site.site_header = "ROLL INDUSTRIES"
admin.site.register(Contact)
