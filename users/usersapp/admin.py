from django.contrib import admin

# Register your models here.
# creation of adatabase tables here for the showing admin pannel using the model
from .models import User, User_Activity, Activity_Periods
admin.site.register(User)
admin.site.register(User_Activity)
admin.site.register(Activity_Periods)