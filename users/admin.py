from django.contrib import admin
from .models import Profile, Skill, Message

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'email']
    list_filter = ['name', 'username', 'email']
    
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['owner', 'name', 'description']
    list_filter = ['owner', 'name']
    
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'subject']
    list_filter = ['sender', 'subject']
