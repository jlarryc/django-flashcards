from django.urls import path, include
from . import views  # added to include views of html pages

urlpatterns = [
	path('', views.home, name="home"),
	path('add', views.add, name="add"),
	path('subtract', views.subtract, name="subtract"),
	path('multiply', views.multiply, name="multiply"),
	path('divide', views.divide, name="divide"),	
]