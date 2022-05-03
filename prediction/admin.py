from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ['user','result']
    ordaring=('user',)
    search_fields=('user',)
