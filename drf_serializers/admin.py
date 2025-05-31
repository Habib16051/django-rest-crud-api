from django.contrib import admin
from drf_serializers.models import Snippet

# Register your models here.
@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'style', 'created')
    search_fields = ('title', 'code')
    list_filter = ('language', 'style')
    ordering = ('-created',)
    readonly_fields = ('created',)

    fieldsets = (
        (None, {
            'fields': ('title', 'code', 'linenos')
        }),
        ('Language and Style', {
            'fields': ('language', 'style')
        }),
        ('Metadata', {
            'fields': ('created',)
        }),
    )