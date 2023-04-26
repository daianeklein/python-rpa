import pyautogui as pa
import time

while True:
    pa.screenshot(f'Printscreen_{time.time()}.png')
    time.sleep(5)
