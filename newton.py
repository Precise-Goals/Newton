
#*******************************************************************************#
#                                            __                                 #
#                        ____  ___ _      __/ /_____  ____                      # 
#                       / __ \/ _ \ | /| / / __/ __ \/ __ \                     #
#                      / / / /  __/ |/ |/ / /_/ /_/ / / / /                     #
#                     /_/ /_/\___/|__/|__/\__/\____/_/ /_/                      #
#                                                                               #
#################################################################################
#                              Required Imports                                 #
#################################################################################

import pyttsx3  
import datetime
import wikipedia 
import webbrowser
import os
import time
import requests
import speech_recognition as sr 
import pyjokes
import pyautogui
import sys
import MyAlaram
import psutil
import speedtest
import json
import random
import pyfiglet
import pywhatkit
from bs4 import BeautifulSoup
from plyer import notification

################################################################################
#                                Voice Engines
################################################################################


voiceEngine = pyttsx3.init('sapi5')
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume', 1)
engine.setProperty('rate',180)


################################################################################
#                                   Functions
################################################################################

def browser():
    chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    print(f"chrome_path")
    return browser()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good Morning!")
        
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon!")

    else:
        speak(f"Good Evening!")

    speak(f"{logindat[0]}! {logindat[2]} ")

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"\nlistening sir .... ")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"\nSarthak: {query}")

    except Exception as e:
        # print(e)
        print("\nSay that again please... ")
        return " "
    return query

def terminator():
            print(f"Closing all Programs")
            os.system("taskkill /f /im Valorant.exe")
            os.system("taskkill /f /im riot.exe")
            os.system("taskkill /f /im WhatsApp.exe")
            os.system("taskkill /f /im Edge.exe")
            os.system("taskkill /f /im Spotify.exe")
            os.system("taskkill /f /im Canva.exe")
            os.system("taskkill /f /im Notion.exe")
            os.system("taskkill /f /im Discord.exe")
            os.system("taskkill /f /im Chrome.exe")
            os.system("taskkill /f /im Code.exe")
            return terminator()

def news():
    main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=ef635c64d7494c5782def6c13ae85b6e"
    main_page = requests.get(main_url).json()
    articles = main_page['articles']
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        print(f"Today's {day[i]} news is {head[i]}")
        speak(f"Today's {day[i]} news is {head[i]}")

 
################################################################################
#                             Main Body of Newton
################################################################################

#                        __
#    ____  ___ _      __/ /_____  ____
#   / __ \/ _ \ | /| / / __/ __ \/ __ \
#  / / / /  __/ |/ |/ / /_/ /_/ / / / /
# /_/ /_/\___/|__/|__/\__/\____/_/ /_/


if __name__ == "__main__":
    logindat = ["sarthak","paradox", "Welcome to the system"] #set your username,password,message here :)
    print("verify your Password... ")
    speak("Verify your Password... ")      
    userinp = takeCommand().lower()  
    for passworddat in logindat:
        if userinp == f"{logindat[1]}":
            wishMe()
            while True:
                
                ####################################################
                #       Some required coding for this purposes     #
                query = takeCommand().lower()
                chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe "
                webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
                sites = [["youtube","https://www.youtube.com"],["stack overflow","https://www.stackoverflow.com"],["google",    "https://www.youtube.com"],["live coaching","https://learn.aakashdigital.com/home/dashboard"],["drive database",    "https://drive.google.com/drive/u/0/my-drive"],["cloud","https://dash.cloudflare.com/login"],["program","https://   github.com/Precise-Goals"],["instagram","https://instagram.com/"]]
                
                
                #####################################################
                #            Functions and Features                 #
                for site in sites:
                    if f'open {site[0]}' in query :
                        speak(f"Opening {site[0]} sir...")
                        webbrowser.open(site[1])
                    elif 'search' in query or 'tell me about' in query or 'grab information' in query or 'what is the' in query or 'what are the' in query or 'find' in query or 'google' in query or 'give infomation' in query:  
                        query = query.replace("search ","")
                        query = query.replace("tell me about ","")
                        query = query.replace("grab information","")
                        query = query.replace("what is the","")
                        query = query.replace("find","")
                        query = query.replace("google","")
                        query = query.replace("give information","")
                        results = wikipedia.summary(query,sentences = 6)
                        speak("According to neurals...")
                        pywhatkit.search(query)
                        print(results)
                        speak(results)
                    elif "youtube" in query or "play video of" in query or "start playing" in query:
                        query = query.replace("youtube","")
                        query = query.replace("play video of","")
                        query = query.replace("start playing","")
                        web  = "https://www.youtube.com/results?search_query=" + query
                        webbrowser.open(web)
                        pywhatkit.playonyt(query)

                    #--------------------------------------------------
                    #                 Apps handler
                    elif 'open code' in query:
                        speak(f"opening Code editor")
                        codePath = "D:\Workspace\Coding\Microsoft VS Code\Code.exe"
                        os.startfile(codePath)  
                    elif 'open spotify' in query:
                        speak(f"opening spotify.")
                        songpath = r"C:\Users\elite\AppData\Roaming\Spotify.exe"
                        os.startfile(songpath)
                    elif 'cross verification' in query:
                        speak(f"Starting verification...")
                        veripath = r"C:\Users\elite\AppData\Local\authy\Authy Desktop.exe"
                        os.startfile(veripath)
                    elif 'open discord' in query:
                        speak(f"Entering communities...")
                        dcpath = r"C:\Users\elite\AppData\Local\Discord\Update.exe"
                        os.startfile(dcpath)
                    elif 'open figma' in query:
                        speak(f"opening figma...")
                        figpath = r"C:\Users\elite\AppData\Local\Figma\app-116.10.9\Figma.exe"
                        os.startfile(figpath)
                    elif 'open notion' in query:
                        speak(f"opening planner...")
                        nopath = r"C:\Users\elite\AppData\Local\Programs\Notion\Notion.exe"
                        os.startfile(nopath)

                    #--------------------------------------------------
                    #                 System Logs

                    elif 'initiate shutdown' in query:
                        speak(f"Good Night bro have a sweet dream")        
                        os.system("shutdown /s /t 2")
                        terminator()
                    elif 'reboot' in query:
                        speak(f"rebooting software...")            
                        os.system("shutdown /r /t 2")
                    elif 'logout' in  query:            
                        speak(f"Logging out soon..")
                        os.system("shutdown -l")
                    elif 'open command' in query:
                        os.system("start cmd")
                    elif 'open graphics panel' in query:
                        speak(f"opening Nvidia Control panel...")
                    elif 'open software edition' in query:
                        speak(f"Opening A.M.D. software adrenaline edition...")
                    elif 'battery status' in query:
                        speak(f"Checking battery status...")
                        time.sleep(1)
                        battery = psutil.sensors_battery()
                        status = battery.percent
                        if status <= 35:
                            speak(f"We need to charge our system sir")
                            print(f"we only have {status} percent battery left \n ")
                        elif status <= 58:
                            speak(f"we need to reduce system usage accordingly sir")
                            print(f"we only have {status} percent battery left \n")
                        elif status <= 100:
                            speak(f"we can use our Full Potential Sir")
                            print(f"we only have {status} percent battery left \n ")
                    elif 'neural power' in query or 'internet status' in query:
                        speak(f"running speed test sir...")
                        st = speedtest.Speedtest(secure=True)
                        dl = st.download() / 1000000
                        ul = st.upload() / 1000000
                        servernames = []
                        st.get_servers(servernames)
                        ping = st.results.ping
                        speak(f'''  Neural Downloading Speed is {dl:.2f} Megabits per seconds 
                                    Neural uploading speed is {ul:.2f} Megabits per seconds 
                                    Neural latency is {ping}''')
                        print(f"neural Downloading speed is {dl:.2f}Megabits per seconds")
                        print(f"neural Downloading speed is {ul:.2f} Megabits per seconds")
                        print(f"neural latency is {ping} milliseconds")
                    elif 'increment neural' in query:
                        pyautogui.press("volumeup")
                    elif 'decrement neural' in query:
                        pyautogui.press("volumedown")
                    elif 'newton mute' in query:
                        pyautogui.press("volumemute")


                    #--------------------------------------------------
                    #               Interactive Stuff

                    elif 'play music' in query:
                        music_dir = 'D:\sharing\Songs'
                        songs = os.listdir(music_dir)
                        print(songs)
                        os.startfile(os.path.join(music_dir, songs[1]))
                    elif 'thought' in query:          
                        with open ('Coding/projects/Nutan/quotes.json','r') as file:
                            quotedata = json.load(file)
                            quotes = quotedata['Quotes']
                            randomise1 = random.choice(quotes)
                            print(randomise1['quote'])
                            print(randomise1['author'])
                            speak(f"| {randomise1['quote']}")
                            speak(f"| {randomise1['author']}")
                    elif 'weather of ' in query: #Take name of city after "weather of" city_name    
                        search = query.replace("weather of","")
                        url = f"https://www.google.com/search?q=weather+of+{search}"
                        r = requests.get(url)
                        soup = BeautifulSoup(r.text,"html.parser")
                        temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
                        description = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
                        
                        weatherdat = description.split('\n')
                        sky = weatherdat[1]
                        times = weatherdat[0]

                        print(f"temperature now in {search} is {temperature}")
                        speak(f"temperature now in {search} is {temperature}") 
                        print(f'Sky can be {sky} throughout {times}')
                        speak(f'Sky can be {sky} throughout {times}')
                    elif 'word art' in query:
                        speak(f"Write a word to be Fontaged :")
                        text = input("What to Design sir : ")
                        resut = pyfiglet.figlet_format( f"{text}" ,font="slant")
                        speak(f"here are the results")
                        print(resut)
                    elif 'jokes' in query:
                        jokes = pyjokes.get_joke("en")
                        print(jokes)
                        speak(jokes)



                        # interactions
                    elif 'set reminder' in query:
                        speak(f"Tell me time when to set reminder")
                        print(f'''In  format of  "set it to 4:50 pm"''')
                        tt = takeCommand().lower()
                        tt = tt.replace("set it to","")
                        tt = tt.replace(".","")      
                        tt = tt.upper()
                        MyAlaram.alaram(tt)
                    elif 'news' in query:
                        speak(f"Grabbing fresh news...")
                        news()
                    elif 'track' in query:
                        speak("let me check bro...")
                        try:
                            ipAdd = requests.get('https://api.ipify.org').text
                            print(ipAdd)
                            geo_requests = requests.get(url)
                            geo_data = geo_requests.json()
                            city = geo_data['city']
                            country = geo_data['country']
                            speak(f"I am not sure but maybe we are in {city} of this {country}")
                        except Exception as e:
                            speak(f"Due to Standby issues i cant fetch data")
                            pass
                    #--------------------------------------------------
                    #          Greeting and talk with Newton

                    elif query in query:
                        with open('Coding/projects/Nutan/chats.json', 'r') as chats:
                            chatdat = json.load(chats)
                            querye = chatdat["Chats"]

                            for chat in querye:
                                if query in chat["query"]:
                                    response = chat["Responses"]
                                    randomres = random.choice(response)
                                    speak(randomres)
                                    print(randomres)
                                    break
                                
                    #--------------------------------------------------
                    #                 Terminations
                    #--------------------------------------------------

                    elif 'terminate all' in query:
                        speak(f"closing all windows...")
                        terminator()
                    elif 'bye newton' in query or 'terminate' in query or 'go now sleep'in query:
                        speak(f"Thanks for using me i am there to help")
                        break
                    break
        else:
            sys.exit()


#                     __  __          __  
#    _________ ______/ /_/ /_  ____ _/ /__
#   / ___/ __ `/ ___/ __/ __ \/ __ `/ //_/
#  (__  ) /_/ / /  / /_/ / / / /_/ / ,<
# /____/\__,_/_/   \__/_/ /_/\__,_/_/|_|
