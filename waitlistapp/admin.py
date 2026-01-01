from django.contrib import admin
from .models import WaitlistSignup

@admin.register(WaitlistSignup)
class WaitlistSignupAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'location', 'farming_type') # Adds the column to the dashboard
