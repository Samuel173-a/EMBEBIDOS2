import time
from gpiozero import LED

led = LED(17)

def leer_intervalo():
    try:
        with open("configuracion.txt", "r") as f:
            return float(f.read().strip())
    except:
        return 1.0 

while True:
    intervalo = leer_intervalo()
    led.on()
    time.sleep(intervalo)
    led.off()
    time.sleep(intervalo)

#Mientras el programa corre en una terminal, abre otra sesión SSH y escribe:
#echo "0.2" > configuracion.txt. Verás que el LED empieza a parpadear más rápido sin reiniciar el script.
