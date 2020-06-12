import pyttsx3
import os
import webbrowser

def speak(tell):
    engine = pyttsx3.init()
    engine.say(str(tell))    
    engine.runAndWait()
print("[1]Search By Using Words \n[2]Search By Using Image: \n")
speak("Press 1 for searching by words and press 2 for searching by using image and 0 for exit")
choice = input()
if choice == "1":
    print("You Choose 1 ready to proceed")
    speak("You Choose 1 ready to proceed")
    word = input("Enter what you wanna search: ")
    print("Command Being Executed")
    speak("Command Being Executed")
    urL='https://www.google.com/search?query='+word
    urL1="https://en.wikipedia.org/wiki/"+word
    chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
    webbrowser.get('chrome').open_new_tab(urL)
    webbrowser.get('chrome').open_new_tab(urL1)
elif choice == "2":
    print("Start Capturing Image...")
    speak("Start Capturing image...")
    os.system("IPCam.py")
    
    
    
