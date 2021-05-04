
import pyautogui as pyauto
import os
import time

#opens the application
def start():
    os.startfile("C:/Users/jayan/AppData/Local/Microsoft/Teams/current/Teams.exe")
    time.sleep(10) #given as a buffer for slow startup

# goes to the webmining team and downloads the latest video
def webmining():
    web_mining=pyauto.locateCenterOnScreen('Web mining team.png') #locates the web mining tile in the teams homescreen
    pyauto.moveTo(web_mining)
    pyauto.click()
    download_button=pyauto.locateCenterOnScreen('download_button.png') #locates the download icon
    pyauto.moveTo(download_button)
    pyauto.click()
    pyauto.alert("Downloading, check downloads folder",timeout=5000)

#driver code
pyauto.alert("This tool downlods the latest video recording from the specified meeting in Microsoft Teams","Teams Downloader v0.1","Continue")
input=pyauto.confirm('Download the latest video from:','Select download option',['Web Mining','Japanese'])
if(input=='Web Mining'):
    start()
    webmining()
