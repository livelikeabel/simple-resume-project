from django.contrib import admin
from .models import Resume, Stack

# Register your models here.
@admin.register(Resume, Stack)
class ResumeAdmin(admin.ModelAdmin):
    pass
