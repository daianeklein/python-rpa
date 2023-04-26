import pyautogui

pyautogui.locateOnScreen("whats_send_button.png")

send_button = pyautogui.locateCenterOnScreen("whats_send_button.png")
pyautogui.moveTo(send_button[0]/2, send_button[1]/2, duration = 1)
pyautogui.click()
pyautogui.click()
