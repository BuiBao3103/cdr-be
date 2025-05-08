from django.contrib import admin
from .models import Intern, Task, Absence

@admin.register(Intern)
class InternAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'uni_code')
    search_fields = ('full_name', 'uni_code')
    list_per_page = 10

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'task_id', 'content', 'project', 'est_time', 'act_time', 'status', 'intern')
    list_filter = ('status', 'date', 'project')
    search_fields = ('task_id', 'content', 'project')
    list_per_page = 10
    date_hierarchy = 'date'

@admin.register(Absence)
class AbsenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'type', 'reason', 'intern')
    list_filter = ('type', 'date')
    search_fields = ('reason', 'intern__full_name')
    list_per_page = 10
    date_hierarchy = 'date'
