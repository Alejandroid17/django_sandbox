from django.contrib import admin

from nested_routers.models import Domain, Nameservers
# Register your models here.

admin.site.register(Domain)
admin.site.register(Nameservers)