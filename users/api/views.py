from django.shortcuts import render
from rest_framework import viewsets
from usersapp.models import User, User_Activity, Activity_Periods  # passe the model class here
from .serializers import Users, User_Act, Userdata
# Create your views here.
# passed the api serializers data to and view
class Userview(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Users

# base on the model and serializers data to api creation
class Useract(viewsets.ModelViewSet):
    queryset = User_Activity.objects.all()
    serializer_class = User_Act

# base on the model and serializers data to api creation
class Userdata(viewsets.ModelViewSet):
    queryset = Activity_Periods.objects.all()
    serializer_class = Userdata