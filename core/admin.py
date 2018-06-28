from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import *


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ('Personal Info', {'fields': ('username', 'password', 'first_name', 'last_name', 'email')}),
        ("Important Date", {'fields': ('last_login', 'date_joined')}),
        ("Grievance App", {'fields': ('projects', 'organisation', 'position')}),
    )


admin.site.register(Project)
admin.site.register(ResponsibleEntity)
admin.site.register(Grievance)
admin.site.register(Case)
admin.site.register(User, CustomUserAdmin)
