from django.contrib import admin
from . models import *
# Register your models here.


class ImageProjectInline(admin.TabularInline):
    model = ImageProject
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ImageProjectInline]


admin.site.register(Contact)
admin.site.register(Profile)
admin.site.register(Service)
admin.site.register(Client)
admin.site.register(Project, ProjectAdmin)


