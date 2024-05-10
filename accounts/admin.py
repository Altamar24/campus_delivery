from django.contrib import admin

from accounts.models import User
from shop.admin import BasketAdmin




@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (BasketAdmin,)

