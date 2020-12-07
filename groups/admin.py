from django.contrib import admin

from . import models


class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

#registering the models    
admin.site.register(models.Group)
