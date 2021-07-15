from math import perm
from subprocess import run
import pyttsx3                       #this library for text to voice generator
import datetime
import speech_recognition as sr
import wikipedia
import smtplib                       #for email
import webbrowser as wb

from wikipedia.wikipedia import search              # for chrome
import os
import pyautogui                                    # for taking screenshot
import psutil                                       # for cpu and bettery update
import pyjokes
from tkinter import *

engine = pyttsx3.init()

# for change voice gender
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# change speed rate (default 200 words per minute)
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S") #strftime --> means convert time in string for speak
    speak(f"the current time is {Time}")

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(f"the current date is {date} {month} {year}")

def wishme():
    speak("Welcome back sir!")
    # time()
    # date()
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    elif hour >= 18 and hour < 24:
        speak("Good evening")
    else:
        speak("Good night")
    speak("Alishka at your service. How can i help you?")

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("test@gmail.com", "123test")
    server.sendmail("text@gmail.com", to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("F:\PYTHON\python_tut\projects\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)

    battery = psutil.sensors_battery
    speak(f"battery is at {battery}")

def jokes():
    speak(pyjokes.get_joke())

def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
        # speak(query)
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query

# takeCommand()
# speak("this is project")
# time()
# date()
# wishme()
def processAudio():
    # run = 1
    if __name__ == "__main__":
        wishme()
        run = 1
        while run == 1:
            query = takeCommand().lower()
            print(query)

            if "hello" in query:
                wishme()

            elif "time" in query:
                time()
            elif "date" in query:
                date()
            elif "offline" in query:
                quit()
            elif "wikipedia" in query:    #error
                speak("Searching...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences = 2)
                speak(result)
            elif "send email" in query:
                try:
                    speak("what should I say?")
                    content = takeCommand()
                    to = "xyz@gmail.com"
                    sendEmail(content)
                except Exception as e:
                    speak(e)
                    speak("Unable to send the message")
            elif "search in chrome" in query:
                speak("What should I search?")
                chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                search = takeCommand().lower()
                wb.get(chromepath).open_new_tab(search+ ".com")
        
            # Not working these statements.........
            # elif "log out" in query:
            #     os.system("shutdown - 1")
            # elif "shutdown" in query:
            #     os.system("shutdown /s /t 1")
            # elif "restart" in query:
            #     os.system("shutdown /r /t 1")
            
            elif "play songs" in query:
                songs_dir = "C:/Users/hp/Music"
                songs = os.listdir(songs_dir)
                os.startfile(os.path.join(songs_dir, songs[0]))

            elif "remember that" in query:
                speak("What should i remember?")
                data = takeCommand()
                speak("you said me to remember" + data)
                remember = open("data.txt","w")
                remember.write(data)
                remember.close()

            elif "do you know anything" in query:
                remember = open("data.txt","r")
                speak("you said me to remember that" + remember.read())
            
            elif "screenshot" in query:
                screenshot()
                speak("Done!")

            elif "cpu" in query:
                cpu()

            elif "joke" in query:
                jokes()
            run+=1

# processAudio()

# def mainScreen():
#     global screen
#     screen = Tk()
#     screen.title("Alishka Assistent")
#     screen.geometry("100x250")

#     nameLabel = Label(text= "Alshka Assistent", width=300, bg= "black", fg="white", font= ("Calibri", 13))
#     nameLabel.pack()

#     microphone_photo = PhotoImage(file= "micro.png")
#     microphone_button = Button(image=microphone_photo, command= processAudio)
#     microphone_button.pack(pady=10)

#     screen.mainloop()

# mainScreen()

screen = Tk()
screen.title("Alishka Assistent")
screen.geometry("450x350")
screen.wm_iconbitmap("microphone.ico")

f1 = Frame(screen, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

nameLabel = Label(f1, text= "Alishka", bg= "grey", fg="black", font= ("Calibri", 20, "bold"))
nameLabel.pack()

textLabel = Label(f1, text= "Your Virtual Assistent", bg= "grey", fg="white", font= ("Calibri", 15, "bold"))
textLabel.pack(pady=70)

button = Button(f1, text= "Close", command= quit, bg="yellow", fg="black", font= ("Calibri", 15))
button.pack(fill=X, side=BOTTOM)

button = Button(f1, text= "Speak", command= processAudio, bg="yellow", fg="black", font= ("Calibri", 15))
button.pack(fill=X, side=BOTTOM)

f2 = Frame(screen, bg="grey", borderwidth=6, relief=SUNKEN)
f2.pack(side=LEFT, fill="y")

microphone_photo = PhotoImage(file= "AI.png")
microphone_photo_label = Label(f2, image=microphone_photo, height=450 ,width=340)
microphone_photo_label.pack(side=LEFT)



screen.mainloop()