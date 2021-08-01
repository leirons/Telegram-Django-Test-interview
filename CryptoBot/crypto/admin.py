from django.contrib import admin

from  .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','name','surname','first_start')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

