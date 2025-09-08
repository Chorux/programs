
import pyautogui
import time
import keyboard
import mouse


liquer = mouse.click ('left')

while True:
    if keyboard.is_pressed('esc'):
        print("Você pressionou 'esc. Saindo...")
        break
    else:
        mouse.click('left')
        print("Clicou")
        time.sleep(0.0)
        
