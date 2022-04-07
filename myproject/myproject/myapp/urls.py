from . import views
from django.urls import path
# from .models import place
# from .models import travellers

urlpatterns = [

    path('', views.demo, name='demo'),
    # path('', views.demo1, name='demo1')

]
