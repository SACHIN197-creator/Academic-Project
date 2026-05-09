from django.contrib import admin
from testapp.models import Enquiry


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'mobile', 'message']


admin.site.register(Enquiry, StudentAdmin)