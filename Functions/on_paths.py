# online function paths

import requests
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
from email.message import EmailMessage
from decouple import config

def find_my_ip():
    ip_address = requests.get("https://api64.ipify.org/?format=json").json()
    return ip_address["ip"]

def search_on_wikipedia(query):
    result = wikipedia.summary(query,sentences=2)
    return result

def play_on_youtube(video):
    kit.playonyt(video)

def search_on_google(query):
    kit.search(query)

def open_youtube():
    webbrowser.open("youtube.com")

def open_google():
    webbrowser.open("google.com")

def open_stackoverflow():
    webbrowser.open("stackoverflow.com")

def open_whatsapp():
    webbrowser.open("whatsapp.com")

def open_facebook():
    webbrowser.open("www.facebook.com")

def send_whatspp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")

def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False   

NEWS_API_KEY = config("NEWS_API_KEY")

def get_latest_news():
    news_headlines = []
    res = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]

OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")

def get_weather_report(city):
    res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}C", f"{feels_like}C"

TMDB_API_KEY = config("TMDB_API_KEY")


def get_trending_movies():
    trending_movies = []
    res = requests.get(f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]

