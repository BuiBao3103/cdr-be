from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Intern, Task, Absence
from .serializers import InternSerializer, TaskSerializer, AbsenceSerializer
from .filters import TaskFilter, AbsenceFilter


class InternViewSet(viewsets.ModelViewSet):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['full_name', 'uni_code']
    ordering_fields = ['id', 'full_name', 'uni_code']


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = TaskFilter
    search_fields = ['task_id', 'content', 'project']
    ordering_fields = ['id', 'date', 'task_id', 'est_time', 'act_time']


class AbsenceViewSet(viewsets.ModelViewSet):
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = AbsenceFilter
    search_fields = ['reason']
    ordering_fields = ['id', 'date', 'type']
