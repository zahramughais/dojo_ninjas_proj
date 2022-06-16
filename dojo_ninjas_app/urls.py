from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('newdojo', views.new_dojo),
    path('addninja', views.add_ninja),
    path('deletedojo/<int:id>', views.del_dojo),
]