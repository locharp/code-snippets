from urllib.request import urlopen
from json import loads

response = urlopen('https://api.open-meteo.com/v1/meteofrance?latitude=55&longitude=25.8&timezone=EET&daily=apparent_temperature_min,apparent_temperature_max')

data = loads(response.read())

daily = data['daily']

day = daily['time']
min = daily['apparent_temperature_min']
max = daily['apparent_temperature_max']

print('{:^10}{:>7}{:>7}'.format('Date', 'Min', 'Max'))
for i in range(4):
    print('{:<10}{:>7}{:>7}'.format(day[i], min[i], max[i]))