import pyttsx3
import datetime
import speech_recognition as sr
import os
import random
import cv2
from decouple import config
from random import choice
from pt import opening_text
from Functions.of_paths import open_camera, open_cmd, open_notepad, open_paint, open_wordpad, open_vscode
from Functions.on_paths import find_my_ip,search_on_wikipedia,search_on_google,play_on_youtube,open_facebook,open_google,open_stackoverflow,open_whatsapp,open_youtube,send_whatspp_message,send_email,get_latest_news,get_weather_report, get_trending_movies

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

# Speech Function

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Wishme Function

def wishme():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"Good Morning {USERNAME}")
    elif hour>=12 and hour<18:
        speak(f"Good Afternoon {USERNAME}")
    else:
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME} Sir. Please Tell Me How May I Help You!")

# Takecommand Function

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        if not 'shut up' in query:
            print(f"User said: {query}\n")
            speak(choice(opening_text))

        else:
            hour = int(datetime.datetime.now().hour)
            if hour>=21 and hour<4:
                speak("Good night sir , take care!")
            else:
                speak("Thanks for using me have a nice day.")
                exit()
        
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

# Main Function

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('what do you want to search on wikipedia, sir?')
            query = takecommand().lower()
            speak('Searching Wikipedia...')
            result = search_on_wikipedia(query)
            speak(f"According to wikipedia, {result}")

        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f"Your IP address is {ip_address}")

        elif 'open youtube' in query:
            open_youtube()

        elif 'open google' in query:
            open_google()
        
        elif 'ok google' in query:
            speak("Sir what should i search on google")
            cmd = takecommand().lower()
            search_on_google(cmd)
        
        elif 'play song on youtube' in query:
            speak("What song do you want to play?")
            cmd = takecommand().lower()
            play_on_youtube(cmd)

        elif 'open stack overflow' in query:
            open_stackoverflow()

        elif 'play music' in query:
            music_dir = 'D:\\old'
            songs = os.listdir(music_dir)
            # print(songs)
            rd=random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        elif 'open vs code' in query:
            open_vscode()
        
        elif 'send email' in query:
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = takecommand().capitalize()
            speak("What is the message sir?")
            message = takecommand().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = takecommand().lower()
            send_whatspp_message(number, message)
            speak("I've sent the message sir.")

        elif 'open notepad' in query:
            open_notepad()

        elif 'open wordpad' in query:
            open_wordpad()

        elif 'open command prompt' in query:
            open_cmd()
        
        elif 'open paint' in query:
            open_paint()

        elif 'open camera' in query:
            open_camera()

        elif 'open whatsapp' in query:
            open_whatsapp()
        
        elif 'open facebook' in query:
            open_facebook()

        elif "open web camera" in query:
            capture=cv2.VideoCapture(0)
            im_count=0
            speak("press the escape for close the camera window and space for clicking a photo.")
            while capture.isOpened():
               ret,img=capture.read()
               if not ret:
                 speak("sorry sir I am not able to grab the camera")
                 break
               
               cv2.imshow('web camera',img)
               m=cv2.waitKey(1)

               if m%256 == 27:
                   break
               elif m%256==32:
                  take_im="E:/python_photo/person_image_{}.png".format(im_count)
                  cv2.imwrite(take_im,img)
                  speak("screen taken")
                  im_count+=1
            capture.release()
            cv2.destroyAllWindows()
        
        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(get_latest_news())
            # print(*get_latest_news(), sep='\n')
        
        elif 'weather' in query:
            speak("Please tell me the location sir: ")
            city = takecommand().lower()
            speak(f"Getting weather report for your city {city}")
            a = get_weather_report(city)
            weather, temperature, feels_like = a
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

        elif "trending movies" in query:
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_trending_movies(), sep='\n')

