import RPi.GPIO as GPIO
import time
# Pin definitions
led_pin = 17
led_pin2 = 27
led_pin3 = 22
led_pin4 = 23
boton1 = 24
boton2 = 25
# Suppress warnings
GPIO.setwarnings(False)
# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)
# Set LED pin as output
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)
GPIO.setup(led_pin3, GPIO.OUT)
GPIO.setup(led_pin4, GPIO.OUT)
GPIO.setup(boton1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(boton2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Blink forever
estado = 0
try:
 while True:
  if GPIO.input(boton1) == GPIO.LOW:
   estado += 1
   if estado > 15:
    estado = 0
   print(f"Dec: {estado:d} | Bin: {estado:04b} | Hex: {estado:X}")
   time.sleep(0.3)

  if GPIO.input(boton2) == GPIO.LOW:
   if estado > 0:
    estado -=1
   print(f"Dec: {estado:d} | Bin: {estado:04b} | Hex: {estado:X}")
   time.sleep(0.3)
  if estado == 0:
   GPIO.output((led_pin, led_pin2, led_pin3, led_pin4), GPIO.LOW)
  elif estado == 1:
   GPIO.output(led_pin4, GPIO.HIGH)
   GPIO.output((led_pin, led_pin2, led_pin3), GPIO.LOW)
  elif estado == 2:
   GPIO.output(led_pin3, GPIO.HIGH)
   GPIO.output((led_pin, led_pin2, led_pin4), GPIO.LOW)
  elif estado == 3:
   GPIO.output((led_pin3, led_pin4), GPIO.HIGH)
   GPIO.output((led_pin, led_pin2), GPIO.LOW)
  elif estado == 4:
   GPIO.output(led_pin2, GPIO.HIGH)
   GPIO.output((led_pin, led_pin3, led_pin4), GPIO.LOW)
  elif estado == 5:
   GPIO.output((led_pin2, led_pin4), GPIO.HIGH)
   GPIO.output((led_pin, led_pin3), GPIO.LOW)
  elif estado == 6:
   GPIO.output((led_pin2, led_pin3), GPIO.HIGH)
   GPIO.output((led_pin, led_pin4), GPIO.LOW)
  elif estado == 7:
   GPIO.output((led_pin2, led_pin3, led_pin4), GPIO.HIGH)
   GPIO.output(led_pin, GPIO.LOW)
  elif estado == 8:
   GPIO.output(led_pin, GPIO.HIGH)
   GPIO.output((led_pin2, led_pin3, led_pin4), GPIO.LOW)
  elif estado == 9:
   GPIO.output((led_pin, led_pin4), GPIO.HIGH)
   GPIO.output((led_pin2, led_pin3), GPIO.LOW)
  elif estado == 10:
   GPIO.output((led_pin, led_pin3), GPIO.HIGH)
   GPIO.output((led_pin2, led_pin4), GPIO.LOW)
  elif estado == 11:
   GPIO.output((led_pin, led_pin3, led_pin4), GPIO.HIGH)
   GPIO.output(led_pin2, GPIO.LOW)
  elif estado == 12:
   GPIO.output((led_pin, led_pin2), GPIO.HIGH)
   GPIO.output((led_pin3, led_pin4), GPIO.LOW)
  elif estado == 13:
   GPIO.output((led_pin, led_pin2, led_pin4), GPIO.HIGH)
   GPIO.output(led_pin3, GPIO.LOW)
  elif estado == 14:
   GPIO.output((led_pin, led_pin2, led_pin3), GPIO.HIGH)
   GPIO.output(led_pin4, GPIO.LOW)
  elif estado == 15:
   GPIO.output((led_pin, led_pin2, led_pin3, led_pin4), GPIO.HIGH)

except KeyboardInterrupt:
 GPIO.cleanup()

