from django.db import models

# Create your models here.
# user vslues model for the database saving data here
class User(models.Model):
    id = models.AutoField(primary_key=True)
    real_name = models.CharField(max_length=50)
    tz   = models.CharField(max_length=100)

    def __str__(self):
        return self.real_name

# user activity model for the database saving the data here
class User_Activity(models.Model):
    Members = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

# activity data creation for the database saving the data here
class Activity_Periods(models.Model):
    users = models.ManyToManyField(User_Activity)



