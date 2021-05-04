import pyautogui as pyauto
import os
import time
os.startfile("C:/Users/jayan/AppData/Local/Microsoft/Teams/current/Teams.exe")
time.sleep(10)
web_mining=pyauto.locateCenterOnScreen('Web mining team.png')
pyauto.moveTo(web_mining)
pyauto.click()
download_button=pyauto.locateCenterOnScreen('download_button.png')
pyauto.moveTo(download_button)
pyauto.click()
pyauto.alert("Downloading, check downloads folder",timeout=5000)

time.sleep(2)