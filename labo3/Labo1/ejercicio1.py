import RPi.GPIO as GPIO
import time
# Pin definitions
led_pin = 27
led_pin2 = 17
boton = 24
# Suppress warnings
GPIO.setwarnings(False)
# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)
# Set LED pin as output
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)
GPIO.setup(boton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Blink forever
try:
    GPIO.remove_event_detect(boton)
except:
    pass

time.sleep(0.1)
estado = 0

def detectar_pulsacion(canal):
    global estado
    estado += 1
    if estado > 4:
        estado = 1
    print(f"Estado{estado}")

def estado_1():
 if estado != 1: return
 GPIO.output(led_pin, GPIO.HIGH)
 GPIO.output(led_pin2, GPIO.LOW)
 time.sleep(1)

 if estado != 1: return
 GPIO.output(led_pin, GPIO.LOW)
 GPIO.output(led_pin2, GPIO.HIGH)
 time.sleep(1)

def estado_2():
 if estado != 2: return
 GPIO.output(led_pin, GPIO.HIGH) # Turn LED on
 GPIO.output(led_pin2, GPIO.HIGH) # Turn LED off
 time.sleep(2)
 if estado != 2: return
 GPIO.output(led_pin, GPIO.LOW) # Turn LED on
 GPIO.output(led_pin2, GPIO.LOW) # Turn LED off
 time.sleep(2)

def estado_3():
    GPIO.output(led_pin, GPIO.HIGH)
    GPIO.output(led_pin2, GPIO.HIGH)

def estado_4():
    GPIO.output(led_pin, GPIO.LOW)
    GPIO.output(led_pin2, GPIO.LOW)

try:
    GPIO.add_event_detect(boton, GPIO.FALLING, callback=detectar_pulsacion, bouncetime=300)
except RuntimeError:
    # Si falla, limpiamos y reintentamos una última vez
    GPIO.cleanup(boton)
    GPIO.setup(boton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(boton, GPIO.FALLING, callback=detectar_pulsacion, bouncetime=300)
try:
 while True:

  if estado == 1:
   estado_1()
  if estado == 2:
   estado_2()
  if estado == 3:
   estado_3()
  if estado == 4:
   estado_4()
  time.sleep(0.1)

except KeyboardInterrupt:
 print("Cerrando")
finally:
 GPIO.cleanup()
