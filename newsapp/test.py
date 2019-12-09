import requests
url='https://openweathermap.org/data/2.5/weather?q=bhopal&appid=b6907d289e10d714a6e88b30761fae22'
r=requests.get(url).json()
#print(r)
a=(r['main']['temp'])
print(a)
