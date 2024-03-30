from django.contrib import admin
from .models import *

# Register your models here.
class RegJobs(admin.ModelAdmin):
    list_display = (
        "name", "description", "due", "status", "author", "worth", "cartegory"
    )
    
admin.site.register(Jobs, RegJobs)