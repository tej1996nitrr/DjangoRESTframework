from rest_framework import serializers
from .models import Language,Paradigm,Programmer

'''
What is serialization?
A serillizer translates to and from json or xml or any other format  which we can send over http
json object is basically composed of the equivalent  of lists and dictionaries
or arrays and objects.We send the list and dict  through requests and then the serilaizer will
deserialize that combination of list and dict into whatever the application object is
In this case language
We cant send the language model directly to the http.it only exts in our app
so we have to send a  common format for data and that common format is json
    
'''
'''
1.make models
2.make serializer
3.make viewsets
4.register routes in urls.py of app

'''
class LanguageSerializer(serializers.HyperlinkedModelSerializer):#shows information relevent to model
    class Meta:
        #necessary specifications
        model = Language
        fields='__all__'
        '''This will translate json into our model '''
class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields ='__all__'

class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields='__all__'

