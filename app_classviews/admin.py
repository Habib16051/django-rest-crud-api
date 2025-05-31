from django.contrib import admin
from .models import Travel
# Register your models here.
@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    """
    Admin interface for the Travel model.
    """
    list_display = ('destination', 'date_start', 'date_end', 'budget')
    search_fields = ('destination',)
    list_filter = ('date_start', 'date_end')
    ordering = ('date_start',)