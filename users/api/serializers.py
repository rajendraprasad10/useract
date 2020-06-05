from rest_framework import serializers
from usersapp.models import User, User_Activity, Activity_Periods

class Users(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class User_Act(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User_Activity
        fields = '__all__'


class Userdata(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity_Periods
        fields = ['users']