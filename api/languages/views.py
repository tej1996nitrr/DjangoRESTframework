from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Language,Paradigm,Programmer
from .serializers import LanguageSerializer,ParadigmSerializer,ProgrammerSerializer
# Create your views here.

'''to handle all types of requests
Instead of defining everything explicitly we inherit the model viewset and it will take care of those things
The only thing we need to specify is how to get an object from the database
It take cares of which methods to use like get,post put etc
'''
class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permisssion_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer






