# weather/urls.py
from django.urls import path
from . import views

# def home(request):
#     return render(request, 'weather/home.html')

urlpatterns = [
    path('', views.inedx, name='index'),
]
