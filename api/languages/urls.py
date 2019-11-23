from django.urls import path,  include
from . import views
from rest_framework import routers
'''routers will take care of generating all the urls'''

router = routers.DefaultRouter()
#register the views
router.register('languages',views.LanguageView)
#1st arg is endoint
# 2nd arg will be the actual view

router.register('programmers',views.ProgrammerView)
router.register('paradigms',views.ParadigmView)
urlpatterns=[
path('',include(router.urls)),
]