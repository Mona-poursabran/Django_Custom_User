from django.contrib import admin
from .models import Topic, Entry
# Register your models here.

admin.site.register(Entry)

class EntryInLine(admin.TabularInline):
    model = Entry

class TopicAdmin(admin.ModelAdmin):
    inlines =[ 
        EntryInLine,
    ]
admin.site.register(Topic, TopicAdmin)