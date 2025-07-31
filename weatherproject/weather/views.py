from django.shortcuts import render
import requests

def home(request):
    weather_data = None

    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'cfd602b5126e293a57cbdc2c965ea43f'  # Replace with your real API key
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {'error': 'City not found'}

    return render(request, 'home.html', {'weather': weather_data})


# Create your views here.
