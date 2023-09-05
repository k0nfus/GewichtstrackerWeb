from django.contrib import admin
from .models import WeightEntry

class WeightEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'weight')  # Die Spalten, die im Admin-Bereich angezeigt werden sollen
    list_filter = ('user', 'date')  # Filteroptionen in der Seitenleiste hinzufügen
    search_fields = ('user__username', 'date')  # Suchfelder hinzufügen

admin.site.register(WeightEntry, WeightEntryAdmin)
