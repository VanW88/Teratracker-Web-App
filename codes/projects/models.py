from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    due_time = models.TimeField()
    supervisor = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['title', 'supervisor'], name="unique title")]
        verbose_name = "Project"

    def __str__(self):
        return str(self.title)
    # + "-" + str(self.supervisor)

# Student in Project
class ProjectStudents(models.Model):
    student = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Project Student"
        constraints = [models.UniqueConstraint(fields=['student', 'project'], name="unique project student")]

    def __str__(self):
        return str(self.project) + "-" + str(self.student)

class Task(models.Model):
    taskname = models.CharField(max_length=50)
    taskdesc = models.TextField(max_length=500)
    sourceproject = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    task_done = models.BooleanField(default=False)
    start_date = models.DateField(default=None)
    start_time = models.TimeField(default=None)
    due_date = models.DateField(default=None)
    due_time = models.TimeField(default=None)
    difficulty = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Task"

    def __str__(self):
        return str(self.taskname)

    def completed(self):
        self.task_done = True

class TaskStudents(models.Model):
    student = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, default=None, on_delete=models.CASCADE)
    plan_percent = models.PositiveIntegerField(default=0)
    time = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Student Task"
        constraints = [models.UniqueConstraint(fields=['student', 'task'], name="unique task student")]

    def __str__(self):
        return str(self.task) + "-" + str(self.student)
