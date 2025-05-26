from django.db import models

# Create your models here.

class TaskStatus(models.TextChoices):
    TO_DO = 'To Do', 'To Do'
    DONE = 'Done', 'Done'

class AbsenceType(models.TextChoices):
    EXCUSED = 'EXCUSED', 'EXCUSED'
    UNEXCUSED = 'UNEXCUSED', 'UNEXCUSED'
    SCHEDULED = 'SCHEDULED', 'SCHEDULED'

class Intern(models.Model):
    full_name = models.CharField(max_length=50)
    uni_code = models.CharField(max_length=10)

    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = "interns"

class Task(models.Model):
    date = models.DateField()
    backlog_id = models.CharField(max_length=10, null=True, blank=True)
    content = models.TextField()
    project = models.CharField(max_length=30, null=True, blank=True)
    estimate_time = models.FloatField()
    actual_time = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=255, choices=TaskStatus.choices, default=TaskStatus.TO_DO)
    intern = models.ForeignKey(Intern, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = "tasks"

class Absence(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=255, choices=AbsenceType.choices)
    reason = models.CharField(max_length=200)
    intern = models.ForeignKey(Intern, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.intern.full_name} - {self.date}"
    
    class Meta:
        db_table = "absences"
