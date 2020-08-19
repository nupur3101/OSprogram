#The os module provides functions for interacting with the Operating System
import os
import pyttsx3       #It is a text-to-speech conversion library
import time

converter = pyttsx3.init()
voices = converter.getProperty('voices')
converter.setProperty('voice',voices[1].id)      # to change the gender of voice--> 0:male, 1:female

converter.runAndWait()
pyttsx3.speak("Hi!! I'm Groovy...  ")

while True:
    print("What can I do for you? ")
    
    p = input().lower()
    
    if ("run" in p) or ("launch" in p) or ("open" in p) or ("play" in p) or ("execute" in p) or ("start" in p):
        
        if ("notepad" in p) or ("text editor" in p) :                                                #notepad
            os.system("notepad")
            
        elif ("chrome" in p) or ("browser" in p) or ("google" in p) or ("search engine" in p):       #chrome
            print("Do you want to open some particular site? Name it : ",end=' ')
            site = input()
            os.system(f"start chrome {site}")
            
        elif ("music" in p) or ("song" in p):                                                        #windows media player
            os.system("start wmplayer")
            
        elif ("paint" in p) :                                                                        #paint
            os.system("start mspaint")
            
        elif ("calculator" in p) or ("calc" in p) or ("cal" in p) :                                  #calculator
            os.system("calc")
            
        elif ("cmd" in p) or ("command prompt" in p) or ("shell" in p):                              #Command prompt
            os.system("start cmd")
            
        elif ("camera" in p):                                                                        #Camera
            os.system("start microsoft.windows.camera:")
            
        time.sleep(1)   
        print()
            
    elif ("quit" in p) or ("exit" in p) or ("close" in p) or("bye" in p):
        print("It was nice chatting with you. Bye...")
        break    
        
    else :
        print("Sorry, I can't understand what you want me to do. Try again :)")
        print()