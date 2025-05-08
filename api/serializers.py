from rest_framework import serializers
from .models import Intern, Task, Absence

class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    intern_name = serializers.CharField(source='intern.full_name', read_only=True)
    
    class Meta:
        model = Task
        fields = '__all__'

class AbsenceSerializer(serializers.ModelSerializer):
    intern_name = serializers.CharField(source='intern.full_name', read_only=True)
    
    class Meta:
        model = Absence
        fields = '__all__' 