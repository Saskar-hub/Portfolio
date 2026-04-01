from django.contrib import admin
from .models import (
    SiteSettings, HeroSection, About, Skill, Project, 
    ProjectImage, Blog, ContactMessage, Testimonial, Experience
)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ('title', 'is_featured', 'category')
    list_filter = ('is_featured', 'category')
    search_fields = ('title', 'description', 'technologies_used')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at')
    list_filter = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_read', 'timestamp')
    list_filter = ('is_read',)
    readonly_fields = ('name', 'email', 'message', 'timestamp')

admin.site.register(SiteSettings)
admin.site.register(HeroSection)
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Testimonial)
admin.site.register(Experience)
