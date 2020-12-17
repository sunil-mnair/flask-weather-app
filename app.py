import json,requests
from flask import Flask,render_template,request

from urllib.request import urlopen


api_key = '2cb5ca9e7bcdd69ad9a80eae91e2c030'

app = Flask(__name__)

@app.route("/")
def index():
    
    
    return render_template("index.html")
    

@app.route("/check_weather",methods=['GET','POST'])
def check_weather():
    
    if request.method == 'POST':
        city = request.form['city']

        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'

        response = requests.get(url)
        data = response.json()

        weather = data["weather"][0]['main']
        current_temp = data["main"]['temp']
        humidity = data["main"]['humidity']

        print(weather)

        with open("weather.json") as file:
            videos = json.load(file)
        
        try:
            video = [video for video in videos['weather'] if video["type"] == weather.lower()][0]
        except:
            print(f"No Video found for Weather Type: {weather} ")
            video = {'video' : 'https://player.vimeo.com/external/363031257.sd.mp4?s=a25de82d147c2bdc6fffa9fa38565cf127ecf3cc&profile_id=139&oauth2_token_id=57447761'}

        print(video)

    return render_template("weather.html",city=city,
    weather = weather,current_temp=current_temp,
    url = video['video'])
    



if __name__ == "__main__":
    app.run(debug=True)