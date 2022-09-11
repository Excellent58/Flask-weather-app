import requests
from flask import Flask, render_template, request, flash
import time
app = Flask(__name__)
app.config['SECRET_KEY'] = "mykey"

@app.route("/", methods=['GET', 'POST'])
def index():
    weather = {}
    t = time.localtime()
    current_time = time.strftime("%H:%M")

    weather['time'] = current_time

    if request.method == "POST":
        city = request.form.get("city")
        
        API_KEY = "f1186383ba40084e342ccc135b8aa771"
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
        request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
        
        try:
            response = requests.get(request_url)

            if response.status_code == 200:
                data = response.json()

                weather['city'] = city
                weather['description'] =  data['weather'][0]['description']
                weather['icon'] = data['weather'][0]['icon']
                weather['temperature'] = round(data["main"]["temp"] - 273.15, 2)
                weather['wind'] = data['wind']["speed"]
                weather['pressure'] = data["main"]["pressure"]
                weather['humidity'] = data["main"]["humidity"]
            else:
                flash("request was not found!!")
        except:
            flash("check your internet connection")

    return render_template("base.html", weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
