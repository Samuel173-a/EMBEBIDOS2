from gpiozero import Buzzer, Button
from signal import pause

buzzer = Buzzer(3)
btn_on = Button(2)
btn_off = Button(4) 

btn_on.when_pressed = buzzer.on
btn_off.when_pressed = buzzer.off

print("Boton 1: ON  Boton 2: OFF")
pause()
