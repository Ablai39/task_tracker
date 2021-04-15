from django.db import models

# class Task(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=60)
#     description = models.CharField(max_length=200)
#     performer = 
#     supervisor
#     status = models.ManyToManyField(Patch_Files, related_name="changed")
#     date_in = models.DateField(verbose_name='Дата загрузки')
#     date_end = models.DateField(blank=True, null=True)
#     date_plan = models.DateField(blank=True, null=True)

# class Change_status(models.Model):
#     previous_status
#     following_status = 
#     task_cs = models.ForeignKey(Task, on_delete=models.CASCADE)
#     changed_by

# class Reminder(models.Model):
#     task_r
#     reminder_text
#     user_list = models.ForeignKey(Change_status, on_delete=models.CASCADE)