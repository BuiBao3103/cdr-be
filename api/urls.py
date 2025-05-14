from django.urls import path
from .views import (
    InternListCreateView, InternDetailView,
    TaskListCreateView, TaskDetailView,
    AbsenceListCreateView, AbsenceDetailView
)

urlpatterns = [
    # Intern URLs
    path('interns/', InternListCreateView.as_view(), name='intern-list-create'),
    path('interns/<int:pk>/', InternDetailView.as_view(), name='intern-detail'),
    
    # Task URLs
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    
    # Absence URLs
    path('absences/', AbsenceListCreateView.as_view(), name='absence-list-create'),
    path('absences/<int:pk>/', AbsenceDetailView.as_view(), name='absence-detail'),
]