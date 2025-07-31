# weather/urls.py
from django.urls import path
from . import views

# def home(request):
#     return render(request, 'weather/home.html')

urlpatterns = [
    path('', views.home, name='index'),
]



#this this file defines the URL patterns for the weather app.# It includes a single path that maps the root URL to the `home` view in the `