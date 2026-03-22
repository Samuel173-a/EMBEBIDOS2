import RPi.GPIO as GPIO
import time 
import random
ven_pin = 17
cal_pin = 27
# Suppress warnings
GPIO.setwarnings(False)
# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)
# Set LED pin as output
GPIO.setup(ven_pin, GPIO.OUT)
GPIO.setup(cal_pin, GPIO.OUT)

print("Sistema de control invernadero")
try:
 while True:
  tempe = random.uniform(5, 30)
  print(f"temperatura{tempe} °C")

  if tempe < 12:
   GPIO.output(cal_pin, GPIO.HIGH)
   GPIO.output(ven_pin, GPIO.LOW)
   print("ventilador prendido")

  elif tempe > 20:
   GPIO.output(cal_pin, GPIO.LOW)
   GPIO.output(ven_pin, GPIO.HIGH)
   print("calentador prendido")

  else:
   GPIO.output(cal_pin, GPIO.LOW)
   GPIO.output(ven_pin, GPIO.LOW)
   print("Estado optimo")
  time.sleep(2)

except KeyboardInterrupt:
    print("Sistema detenido")
finally:
    # Limpieza de pines para seguridad
    GPIO.cleanup()
