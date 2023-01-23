from microbit import *
walks=0
accelerometer_history_x=accelerometer.get_x()
while True:
    accelerometer_now_x=accelerometer.get_x()
    if abs(accelerometer_history_x-accelerometer_now_x)>350:
        walks=walks+1
    accelerometer_history_x=accelerometer_now_x
    if button_a.is_pressed():
        walks=0
    if button_b.is_pressed():
        display.scroll(str(walks))
