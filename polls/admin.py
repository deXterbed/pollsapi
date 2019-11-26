from django.contrib import admin

from .models import Poll, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date', 'created_by')
    list_filter = ['pub_date']
    search_fields = ['question']
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Author', {'fields': ['created_by']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
