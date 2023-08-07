from django.contrib import admin

# Register your models here.

from .models import User, Follower

admin.site.register(User)
admin.site.register(Follower)