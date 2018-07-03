import pyowm
 
owm = pyowm.OWM('3817f5e71da546936ec5da9c401e9f44')
observation = owm.weather_at_place('Accra,GH')
w = observation.get_weather()
 
wind = w.get_wind()
humidity = w.get_humidity()
print(wind)
print(humidity)
