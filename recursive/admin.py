from django.contrib import admin

from recursive.models import Recursive1, Recursive2, Recursive2Throught
# Register your models here.

admin.site.register(Recursive1)
admin.site.register(Recursive2)
admin.site.register(Recursive2Throught)