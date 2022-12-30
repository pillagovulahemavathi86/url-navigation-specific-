from django.urls import path
from app.views import *
app_name='homepage'

urlpatterns=[
    path('python/',python,name='python'),
    path('details/',details,name='details'),
]