import pyautogui as pa

pa.PAUSE = 2

distance = 200

initial_distance = (373, 526)
second_distance = (569, 490)
third_distance = (561, 587)


times = 0
while times < 1:
    pa.moveTo(initial_distance)
    pa.click()
    pa.dragTo(second_distance, button = 'left', duration = 0.1)
    pa.dragTo(third_distance, button = 'left', duration = 0.1)
    pa.dragTo(initial_distance, button = 'left', duration = 0.1)

    times += 1