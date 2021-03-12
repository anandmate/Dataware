from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin


# Register your models here.

@admin.register(Php, Html, Css, Wordpress, Bootstrap, Rtool, Python, Stat, Machine)
class ViewAdmin(ImportExportActionModelAdmin):
    pass
