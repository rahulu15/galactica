from django.contrib import admin

from . import models
#registering post model
admin.site.register(models.Post)
