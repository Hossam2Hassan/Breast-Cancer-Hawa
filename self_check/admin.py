from django.contrib import admin

# Register your models here.
from .models import Self_checkModel,CheckingModel,CalendarModel


@admin.register(Self_checkModel)
class exam(admin.ModelAdmin):
    list_display=['question']



@admin.register(CheckingModel)
class check(admin.ModelAdmin):
    list_display=['self_check','user','answer','date',]


@admin.register(CalendarModel)
class data(admin.ModelAdmin):
    list_display = ['self_check','period']