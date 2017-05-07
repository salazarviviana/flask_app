from flask import Flask, render_template, request
import weather
import os

app = Flask(__name__)

@app.route("/")  # crea una pagina. esta es el home
def index():   #name of the function to call the page index in html
    name = request.values.get('name')  #.values returns a dictionary. With .get we are looking for the 'name' key. If do not exist .get will return 'none'
    address = request.values.get('address')
    if address:
    	forecast = weather.get_weather(address)
    else:
    	address = "New York, NY"
    	forecast = weather.get_weather(address)
    return render_template('index.html', name = name, forecast = forecast)	#calls the html file ans sending through the variable name, with the value name found before

@app.route("/about")  # crea otra pagina. Esta es el About
def about():   #name of the function to call the page about in html
    return render_template('about.html')	#calls the html file	

if __name__ == "__main__":
    #app.run()  #when wokring on a local port
    port = int(os.environ.get("PORT", 5000))  #when deploying it to Heroku
    app.run(host="0.0.0.0", port=port)


# result:  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)