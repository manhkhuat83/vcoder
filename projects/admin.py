from django.contrib import admin
from .models import Project, Tag, Review

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created']
    list_filter = ['title', 'created']
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created']
    list_filter = ['name',]
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'created']
    list_display = ['project',]
