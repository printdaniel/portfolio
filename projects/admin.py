from django.contrib import admin
from .models import Project, ProjectMedia

class ProjectMediaInline(admin.TabularInline):
    model = ProjectMedia

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectMediaInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectMedia)
