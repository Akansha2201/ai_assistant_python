# Import necessary modules
import pyttsx3 as p
import speech_recognition as sr
from seleniumWeb import *
from YoutubeAudio import *
from newsAPI import *
import randfacts
from joke import *
from weatherAPI import *
import datetime
from sendEmail import *

# Initialize text-to-speech engine
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

# Define function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Get current date and time
today_dateTime = datetime.datetime.now()
today_date = today_dateTime.strftime("%d of %B")
current_time = today_dateTime.strftime("%I:%M %p")

# Greet the user based on the time of the day
def get_time_of_day():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 17:
        return "Good afternoon"
    elif 17 <= current_hour < 20:
        return "Good evening"
    else:
        return "Hi"

time_of_day = get_time_of_day()

# Define function to listen for wake word
def listen_wake_word():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening for wake word..")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio).lower()
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError as e:
        print("Request error; {0}".format(e))
        return ""

# Listen for wake word
wake_word = ""
while wake_word != "wake up":
    wake_word = listen_wake_word()

speak(time_of_day)
speak("I am your voice assistant, Meera.")
speak("It's " + today_date + " today and time is " + current_time)
speak("How are you?")

# Define function to listen for user commands
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening..")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio).lower()
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError as e:
        print("Request error; {0}".format(e))
        return ""
    
command = listen()
if "what about you" in command:
        speak("I am having a good day. Thank You")
     
elif "how about you" in command:
        speak("I am having a good day. Thank You")
             
# Main functionality loop

while True:
    speak("What can I do for you?")
    command = listen()
    
    # For asking questions

    if "information" in command:
        speak("You need information about which topic?")
        topic = listen()
        speak("Sure, searching {} in wikipedia".format(topic))
        assist = info()
        assist.get_info(topic)
        pass
        
    elif "what is" in command:
        topic = command.split("tell me about")[1].strip()
        speak("Sure, searching {}".format(topic))
        assist = info()
        assist.get_info(topic)
        pass
    
    elif "tell me about" in command:
        topic = command.split("tell me about")[1].strip()
        speak("Sure, searching {}".format(topic))
        assist = info()
        assist.get_info(topic)
        pass
        
    # For plaing songs and videos
    
    elif "play video song" in command:
        speak("Sure, what do you want me to play?")
        video = listen()
        speak(f"Sure, searching {video} on YouTube.")
        assist = music()
        assist.play(video)
        pass
    
    # For narrating news, facts and jokes
    
    elif "news" in command:
        speak("Sure, Todays headlines are")
        newsHeadLines = news()
        for i in range(len(newsHeadLines)):
            print(newsHeadLines[i])
            speak(newsHeadLines[i])
        pass
    
    elif "fact" in command:
        speak("Sure, here's a random fact.")
        fact = randfacts.getFact()
        print(fact)
        speak(fact)
        pass
    
    elif "joke" in command:
        speak("Sure, get ready for some chuckles.")
        arr = joke()
        print(arr[0])
        speak(arr[0])
        print(arr[1])
        speak(arr[1])
        pass
    
    # For sending email
        
    elif "email" in command:
        speak("Sure, please provide the email subject.")
        subject = listen()
        speak("Now, please provide the email message.")
        message = listen()
        speak("Finally, please provide the recipient's email address.")
        recipient_email = listen()
        send_email(subject, message, recipient_email)
        speak("Email sent successfully!")
        pass
    
    # For creating reminders and alarm
        
    elif "alarm" in command:
        speak("Sure, when do you want to set the alarm?")
        speak("Please specify the time in 24-hour format, for example, 7:30 or 15:45.")
        time_input = listen()
        try:
            hour, minute = map(int, time_input.split(':'))
            if 0 <= hour < 24 and 0 <= minute < 60:
                speak("Alarm set for {}:{}.".format(hour, minute))
                while True:
                    current_time = datetime.datetime.now()
                    if current_time.hour == hour and current_time.minute == minute:
                        speak("Alarm! It's {}:{}.".format(hour, minute))
                        break
                break
            else:
                speak("Invalid time. Please specify the time again.")
        except ValueError:
            speak("Invalid input. Please specify the time in the correct format.")

    elif "reminder" in command:
        speak("Sure, what's the reminder?")
        reminder = listen()
        speak("When do you want to be reminded?")
        speak("Please specify the time in 24-hour format, for example, 7:30 or 15:45.")
        time_input = listen()
        try:
            hour, minute = map(int, time_input.split(':'))
            if 0 <= hour < 24 and 0 <= minute < 60:
                speak("Reminder set for {}:{}.".format(hour, minute))
                while True:
                    current_time = datetime.datetime.now()
                    if current_time.hour == hour and current_time.minute == minute:
                        speak("Reminder: {}".format(reminder))
                        break
                break
            else:
                speak("Invalid time. Please specify the time again.")
        except ValueError:
            speak("Invalid input. Please specify the time in the correct format.")
            
    # For exiting tool without any command

    elif "exit" in command:
        speak("Goodbye!")
        break
