from django.contrib import admin
from .models import Course, Note
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['className', 'professor', 'section']
    list_filter = ['className']
    search_fields = ['className', 'professor']

admin.site.register(Note)