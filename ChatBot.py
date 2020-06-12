import os
import webbrowser
from datetime import datetime
from datetime import date
import sys
import pyttsx3
import cv2
from colorama import init,Fore, Back, Style 
from playsound import playsound
init(convert=True)
print(Fore.GREEN+"\t###########################################################################################################")
print("\t###########################      #######      ######        #####   ######   ##############################")
print("\t###########################  ####  ####  ####  ####   ###########   #####   ###############################")
print("\t###########################  ####  ####  ####  ####   ###########   ####  #################################")
print("\t###########################       #####        ####   ###########       ###################################")
print("\t###########################  ####  ####  ####  ####   ###########   ###   #################################")
print("\t###########################  ####  ####  ####  ####   ###########   #####   ###############################")
print("\t###########################       #####  ####  ####         #####   ######   ##############################")
print("\t###########################################################################################################")
print("\t###########################################################################################################")
print("\t###########################################################################################################")
print("\t#####      ####         ####    ######  #####      #####  #####  ###         ####        #####         ####")
print("\t#####  ###  ###  ###########  ##  ####  ####   #########  #####  ###  ###########  ####   ####   ####  ####")
print("\t#####  ###  ###  ###########  ###  ###  ###   ##########  #####  ###  ###########  ###   ######   #########")
print("\t#####     #####       ######  ####  ##  ###  ###########         ###      #######    ############    ######")
print("\t#####  ###  ###  ###########  #####  #  ###  ###########  #####  ###  ###########  ##   ############    ###")
print("\t#####  ###  ###  ###########  ######    ###   ##########  #####  ###  ###########  ###   #####  ######    #")
print("\t#####      ####         ####  #######   #####      #####  #####  ###         ####  #####   ####           #")
print("\t###########################################################################################################")
print("\t###########################################################################################################")
def speak(tell):
	engine = pyttsx3.init()
	engine.say(str(tell))    
	engine.runAndWait()
print(Fore.RED+"NOTE: Use 'Help' for list of Commands")
print(Fore.BLUE+"Enter Your Name:")
name = str(input())
print(Fore.BLUE+"Welcome Mr."+name.upper()+" Sir")
speak("Welcome Mr."+name+"Sir")
while True:
	data = input(name.upper()+ ": " )
	if data.lower() in ["what is date","time","date","show date","today datetime","datetime","today date","today"]:
		if data.lower() in ["time","what is time","show time"]:
			currentDT = datetime.now()
			print(currentDT.strftime("%I:%M:%S %p"))
			speak(currentDT.strftime("%I:%M:%S %p"))
		else:
			today = date.today()
			print("Bot: "+today.strftime("%B %d, %Y"))
			speak(today.strftime("%B %d, %Y"))
	if data.lower()=="ipcam":
		print("Bot: Openning IPCam Detector..")
		speak("Openning IPCam Detector..")
		os.sysemt('cmd /k "IPCam.py"')
		print(Fore.RED+'exiting module')
		speak("exiting module")
		os.system("cls")
	if data.lower()=="image":
		print("Bot: Openning image Detector..")
		speak("Openning image Detector..")
		os.system("Image.py")
		print(Fore.RED+"exiting module")
		speak("exiting module")
		os.system("cls")
	if data.lower()=="webcam":
		print("Bot: Openning webcam Detector..")
		speak("Openning webcam Detector..")
		os.system("WebCam.py")
		print(Fore.RED+"Bot: exiting module")
		speak("exiting module")
		os.system("cls")
	if data.lower() in ["play music","music play","music"]:
		print("Choose Offline or Online Music Player")
		speak("Choose Offline or Online Music Player")
		print("[1] For Offline \n[2] For Online")
		speak("[1] For Offline \n [2] For Online")
		choice = str(input())
		if choice == "1":
			print("playing imagine dragon Believer song from music directory")
			speak("playing imagine dragon Believer song from music directory")
			playsound("M0usic/Believer.mp3")
			os.system("cls")
		if choice == '2':
			print("Enter name of the song to find")
			speak("Enter name of the song to find")
			word=str(input())
			print("Going to search on web")
			speak("Going to search on web")
			urL="https://www.jiosaavn.com/search/"+word
			chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
			webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
			webbrowser.get('chrome').open_new_tab(urL)
			os.system("cls")
		else :
			print(Fore.RED+"Wrong Input exiting module....")
			speak("Wrong Input exiting module")
			os.system("cls")
	if data.lower()=="search":
		print("Search Your Query On Web")
		speak("Search Your Query On Web")
		os.system("Search.py")
		os.system("cls")
	if data.lower() in ["what you can do","what you can do for me","help"]:
		print("Execution     \t                 Commands")
		print("[1]Access IPcam Detector \t ipcam \n[2]Access WebCam Detector\t webcam \n[3]Access Image Detector\t image \n[4]Chat With Bot \t        'say hii!' \n[5]Search Query On Web \t         search \n[6]Play Music Online & Offline \t play music \n[7]Video Object Detector\t Video \n[8]Top News      \t         news \n")
		speak("[1]Access IPcam Detector \n[2]Access WebCam Detector \n[3]Access Image Detector \n[4]Chat With Bot \n[5]Search Query On Web \n[6]Play Music Online & Offline \n[7]Video Object Detector \n [8]Today's Top News")

	if data.lower() in ["bye","tata","exit"]:
		print(Fore.RED+"Bye Bye Have A Good Day "+name+" sir")
		speak("Bye Bye Have A Good Day "+name+" sir")
		break
	if data.lower() in ['news','play news']:
		os.system("News.py")		
	if data.lower() in ['video','Play video']:
		print("Preparing Video For detection")
		speak("Preparing Video For detection")
		os.system("Video.py")

	

		
		




	
