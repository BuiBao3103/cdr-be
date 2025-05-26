from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Intern, Task, Absence
from .serializers import InternSerializer, TaskSerializer, AbsenceSerializer
from .filters import TaskFilter, AbsenceFilter
from .pagination import CustomPagination


class InternListCreateView(generics.ListCreateAPIView):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['full_name', 'uni_code']
    ordering_fields = ['id', 'full_name', 'uni_code']
    pagination_class = CustomPagination


class InternDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = TaskFilter
    search_fields = ['backlog_id', 'content', 'project']
    ordering_fields = ['id', 'date', 'backlog_id', 'estimate_time', 'actual_time']
    pagination_class = CustomPagination


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class AbsenceListCreateView(generics.ListCreateAPIView):
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = AbsenceFilter
    search_fields = ['reason']
    ordering_fields = ['id', 'date', 'type']
    pagination_class = CustomPagination


class AbsenceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer
