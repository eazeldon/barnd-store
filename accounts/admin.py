from django.contrib import admin
#to fix the password in the admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile
from django.utils.html import format_html

from .models import Account

# Register your models here.

#--Admin fieldsets to make the password read only
#--email, first name and date joined to be click
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'date_joined')
    ordering = ('date_joined',)
     
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
 #sect-23-len107-class
class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object): #- show profile pic
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture' #- title of the picture
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')

       
admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
