from django.contrib import admin

from django.contrib.auth.models import User
from people.models import UserInfo
from food.models import Order


class UserInfoInline(admin.TabularInline):
    model = UserInfo


class OrderInline(admin.TabularInline):
    extra = 0
    model = Order


class UserAdmin(admin.ModelAdmin):
    model = User
    inlines = [
        UserInfoInline,
        OrderInline
    ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
