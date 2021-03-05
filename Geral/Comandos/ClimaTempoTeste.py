import requests as rq

cidade = 'salvador'

def clima_tempo():
	endereco_api = "http://api.openweathermap.org/data/2.5/weather?appid=5600ff2f7fb3d163a1b20079b9a063dc&q="
	url = endereco_api + cidade

	infos = rq.get(url).json()


	# Coord
	longitude = infos['coord']['lon']
	latitude = infos['coord']['lat']
	# main
	temp = infos['main']['temp'] - 273.15 # Kelvin para Celsius
	pressao_atm = infos['main']['pressure'] / 1013.25 #rLibas para ATM
	umidade = infos['main']['humidity'] # Recebe em porcentagem
	temp_max= infos['main']['temp_max'] - 273.15 # Kelvin para Celsius
	temp_min = infos['main']['temp_min'] - 273.15 # Kelvin para Celsius

	#vento
	v_speed = infos['wind']['speed'] # km/ h

	#clouds / nuvens

	nebulosidade = infos['clouds']['all']

	return [longitude, latitude,
		temp, pressao_atm, umidade,
		temp_max, temp_min, v_speed,
		 nebulosidade]

x = clima_tempo()
print(x)