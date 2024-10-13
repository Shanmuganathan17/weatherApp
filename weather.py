from flask import Flask, render_template, request 

# import json to load JSON data to a python dictionary 
import json 

# urllib.request to make a request to api 
import urllib.request 



app = Flask(__name__) 

@app.route('/', methods =['POST', 'GET']) 
def weather(): 
	if request.method == 'POST': 
		city = request.form['city'] 
	else: 
		# for default name mathura 
		city = 'mathura'

	# your API key will come here 
	api = '619a0de80805922cd5b2fd2591046864' 

	# source contain json data from api 
	source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api).read() 

	# converting JSON data to a dictionary 
	list_of_data = json.loads(source)
	print(str(list_of_data['weather'][0]['main']))
	print(str(list_of_data['weather'][0]['description']))
	# data for variable list_of_data 
	data = { 
		"country_code": str(list_of_data['sys']['country']), 
		"coordinate": str(list_of_data['coord']['lon']) + ' '
					+ str(list_of_data['coord']['lat']),
		"Weather":str(list_of_data['weather'][0]['main']),
		"Weather_Description":str(list_of_data['weather'][0]['description']),
		"cityname": str(list_of_data['name']),
		"temp": str(list_of_data['main']['temp']) + 'k', 
		"pressure": str(list_of_data['main']['pressure']), 
		"humidity": str(list_of_data['main']['humidity']), 
	} 
	print(data) 
	return render_template('index.html', data = data) 



if __name__ == '__main__': 
	app.run(debug = True) 
