import subprocess
import pyttsx3
import speech_recognition as sr
import datetime
import random

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def respond_to_greeting():
    greetings = ["Hello!", "Hi there!", "Greetings!", "How can I assist you today?"]
    return random.choice(greetings)

def get_time():
    now = datetime.datetime.now()
    return now.strftime("The current time is %H:%M:%S")

def open_application(app_name):
    try:
        if app_name.lower() == 'youtube':
            subprocess.run(["start", "https://www.youtube.com"], shell=True)
        elif app_name.lower() == 'notepad':
            subprocess.run(["notepad.exe"])
        elif app_name.lower() == 'calculator':
            subprocess.run(["calc.exe"])
        else:
            return f"Sorry, I don't know how to open {app_name}."
        return f"Opening {app_name}..."
    except Exception as e:
        return f"Failed to open {app_name}. Error: {e}"

def restart_computer():
    try:
        subprocess.run(["shutdown", "/r", "/t", "0"])
        return "Restarting the computer..."
    except Exception as e:
        return f"Failed to restart the computer. Error: {e}"

def listen_for_commands():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            return command
        except sr.UnknownValueError:
            return "Sorry, I did not understand that."
        except sr.RequestError:
            return "Sorry, there was an issue with the request."

def main():
    speak("Jarvis at your service. Please give me a command.")
    
    while True:
        command = listen_for_commands()
        print("You said:", command)
        
        if "hi" in command or "hello" in command or "hey" in command:
            speak(respond_to_greeting())
        
        elif "time" in command or "what time is it" in command:
            speak(get_time())
        
        elif "open" in command:
            app_name = command.replace("open", "").strip()
            speak(open_application(app_name))
        
        elif "restart" in command:
            speak(restart_computer())
        
        elif "exit" in command:
            speak("Goodbye!")
            break
        
        else:
            speak("I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
