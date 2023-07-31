from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser
    list_display=[
        "email",
        "username",
        "name",
        "is_staff"
    ]
    """
    fieldsets are list of fields displayed together in user detail view and user creation view in django admin interface. 
    fieldsets are group of various fields. 
    UserAdmin.fieldsets  is the default fieldsets attribute defined in built in UserAdmin Class
    ((None,{"fields":("name",)}),) IS A TUPLE CONTAINING new fieldset.
    The None represents fieldset's title. 
    {"fields":("name",)} is a dictionary specifying the fields to be included in this fieldset
    We add this to the UserAdmin.fieldsets
    The fieldsets attribute is used when displaying detailed view of a user, showing various
    sections of user information grouped together. 
    """
    fieldsets=UserAdmin.fieldsets+((None,{"fields":("name",)}),)
    """
    The purpose of the below statement is to customize the fieldsets for the user creation view in 
    django admin interface. The add_fieldsets attribute is used when creating a new user from the admin
    interface. BBy adding the "name" field to the add_fieldsets, administrators can input the name while creating a new user record
    """
    add_fieldsets=UserAdmin.add_fieldsets+((None,{"fields":("name",)}),)

#Register with admin interface to manage and interact with user data
admin.site.register(CustomUser,CustomUserAdmin)
