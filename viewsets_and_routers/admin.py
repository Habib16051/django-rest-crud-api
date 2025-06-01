from django.contrib import admin
from .models import Cricket

# Register your models here.
@admin.register(Cricket)
class CricketAdmin(admin.ModelAdmin):
    list_display = ('player_name', 'team_name', 'runs_scored', 'wickets_taken', 'match_date')
    search_fields = ('player_name', 'team_name')
    list_filter = ('team_name', 'match_date')
    ordering = ('-match_date',)