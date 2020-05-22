from django.contrib import admin

from .models import Comments, Forum, Section, Subject

admin.site.register(Comments)
admin.site.register(Forum)
admin.site.register(Section)
admin.site.register(Subject)
