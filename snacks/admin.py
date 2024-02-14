from django.contrib import admin
from .models import Snack

class SnackAdmin(admin.ModelAdmin):
    list_display = ('title', 'purchaser', 'description')

admin.site.register(Snack)