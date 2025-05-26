from django_filters import rest_framework as filters
from .models import Task, Absence, TaskStatus, AbsenceType

class TaskFilter(filters.FilterSet):
    date_from = filters.DateFilter(field_name='date', lookup_expr='gte', label='Date From')
    date_to = filters.DateFilter(field_name='date', lookup_expr='lte', label='Date To')
    intern_name = filters.CharFilter(field_name='intern__full_name', lookup_expr='icontains', label='Intern Name')
    intern_id = filters.NumberFilter(field_name='intern__id', label='Intern ID')
    backlog_id = filters.CharFilter(field_name='backlog_id', lookup_expr='icontains', label='Task ID')
    content = filters.CharFilter(field_name='content', lookup_expr='icontains', label='Content')
    project = filters.CharFilter(field_name='project', lookup_expr='icontains', label='Project')
    status = filters.ChoiceFilter(choices=TaskStatus.choices, label='Status')
    estimate_time_min = filters.NumberFilter(field_name='estimate_time', lookup_expr='gte', label='Min Estimated Time')
    estimate_time_max = filters.NumberFilter(field_name='estimate_time', lookup_expr='lte', label='Max Estimated Time')
    actual_time_min = filters.NumberFilter(field_name='actual_time', lookup_expr='gte', label='Min Actual Time')
    actual_time_max = filters.NumberFilter(field_name='actual_time', lookup_expr='lte', label='Max Actual Time')

    class Meta:
        model = Task
        fields = {
            'status': ['exact'],
            'project': ['exact', 'icontains'],
            'intern': ['exact'],
            'intern_id': ['exact'],
            'date': ['exact', 'gte', 'lte'],
            'backlog_id': ['exact', 'icontains'],
            'content': ['exact', 'icontains'],
            'estimate_time': ['exact', 'gte', 'lte'],
            'actual_time': ['exact', 'gte', 'lte'],
        }

class AbsenceFilter(filters.FilterSet):
    date_from = filters.DateFilter(field_name='date', lookup_expr='gte', label='Date From')
    date_to = filters.DateFilter(field_name='date', lookup_expr='lte', label='Date To')
    intern_name = filters.CharFilter(field_name='intern__full_name', lookup_expr='icontains', label='Intern Name')
    intern_id = filters.NumberFilter(field_name='intern__id', label='Intern ID')
    type = filters.ChoiceFilter(choices=AbsenceType.choices, label='Type')
    reason = filters.CharFilter(field_name='reason', lookup_expr='icontains', label='Reason')

    class Meta:
        model = Absence
        fields = {
            'type': ['exact'],
            'intern': ['exact'],
            'intern_id': ['exact'],
            'date': ['exact', 'gte', 'lte'],
            'reason': ['exact', 'icontains'],
        } 