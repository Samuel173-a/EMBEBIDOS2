from gpiozero import Buzzer, button
from signal import pause

buzzer = Buzzer(3)
button = Button(2)

button.when_pressed = buzzer.on
button.when_released = buzzer.off

print("Presiona el boton para sonar")
pause()
