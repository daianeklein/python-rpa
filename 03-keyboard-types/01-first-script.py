import pyautogui
import time

#send_button = pyautogui.locateCenterOnScreen("whats_send_button.png")
#pyautogui.moveTo(send_button[0]/2, send_button[1]/2, duration = 1)

type_message = pyautogui.locateCenterOnScreen('write_message.png', grayscale = True)
pyautogui.moveTo(type_message[0]/2, type_message[1]/2, duration = 1)
pyautogui.click()

pyautogui.typewrite('Mensagem Automatica: Julianão! (esse pode ir pro Git). Fim da mensagem automática')
time.sleep(2)
send_button = pyautogui.locateCenterOnScreen("whats_send_button.png", grayscale= True)
pyautogui.moveTo(send_button[0]/2, send_button[1]/2, duration = 1)
pyautogui.click()