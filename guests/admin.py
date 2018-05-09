# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from guests.models import Labels, Guest, Information_Broadcast

# Register your models here.


admin.site.register(Labels)
admin.site.register(Guest)
admin.site.register(Information_Broadcast)