from flask import Flask, redirect, render_template, request, session, url_for, flash
from flask_mail import Mail, Message
from urllib import response
import requests

API_KEY = "2be556f4759ac4ac92bcf97767cbdd1f"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

#Configs
app = Flask('mailer')
app.secret_key = "234F6C69766572536D656C6C794146"
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'kurzeschwanz@gmail.com'
app.config['MAIL_PASSWORD'] = 'UCIChamps18'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

Mail = Mail(app)

#index page
@app.route("/", methods=['POST', 'GET'])
def index():
    #check for a post request
    if request.method == "POST":
        #recieve city data
        city = request.form['city']
        flash("something happened")
        #redirect to data generation
        return redirect(url_for('data', city=city))
    else:
        return render_template('index.html')

@app.route('/<city>', methods=['POST', 'GET'])
def data(city):
    if request.method == "POST":
        if "data" in session:
            return redirect(url_for('mail'))
        else:
            flash("No data generated")

    #generate a url to API with a query for city
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&lang=cz&units=metric&exclude=minutely"
    response = requests.get(request_url)

    #if server responds with 200, proceed
    if response.status_code == 200:
        #store response in JSON format
        data = response.json()

        #Parsing data to render easier
        mWeather = data['weather'][0]['main'] 
        deWeather = data['weather'][0]['description']
        temp = str(round(data['main']['temp'], 2)) + "°C"
        feelTemp = str(round(data['main']['feels_like'], 2)) + "°C"
        lon = str(data['coord']['lon'])
        lat = str(data['coord']['lat'])

        session["data"] = data
        
        #render data
        return render_template('data.html', city=city, mWeather=mWeather, deWeather=deWeather,
                                temp=temp, lon=lon, lat=lat, feelTemp=feelTemp, data=data)
    else:
        flash("An error occured", "info")
        redirect(url_for('index'))

@app.route('/mail')
def mail():
    data = session['data']
    msg = Message('Hello, Not A Teapot',
    sender = 'kurzeschwanz@gmail.com',
    recipients = ['kurzeschwanz@gmail.com'])
    msg.html = f"<h1>Present your cakes</h1> <h2>{data}"
    
    Mail.send(msg)
    return "<h1>Check ur inbox!</h1>"

if __name__ == '__main__':
    app.run(debug = True)