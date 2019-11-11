# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from permission.models import Role

# Register your models here.

class RoleAdmin(admin.ModelAdmin):
    filter_horizontal = ('permissions','groups')

admin.site.register(Role,RoleAdmin)