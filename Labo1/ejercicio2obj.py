import RPi.GPIO as GPIO
import time

class ContadorBinario:
    def __init__(self, pines_leds, pin_btn1, pin_btn2):
        # Atributos del objeto
        self.leds = pines_leds
        self.btn_inc = pin_btn1
        self.btn_dec = pin_btn2
        self.estado = 0
        # Configuración inicial de GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        # Configurar LEDs como salida
        for pin in self.leds:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

        # Configurar Botones como entrada
        GPIO.setup(self.btn_inc, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.btn_dec, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def mostrar_consola(self):

        print(f"Dec: {self.estado:d} | Bin: {self.estado:04b} | Hex: {self.estado:X}")

    def actualizar_leds(self):
        """Actualiza los LEDs físicos basándose en el estado actual usando bits."""
        # Usamos operaciones de bits para evitar los 16 if/elif. 
        # Esto es mucho más eficiente y profesional.
        GPIO.output(self.leds[3], (self.estado >> 0) & 1) # LED4 (Bit 0 - el de la derecha)
        GPIO.output(self.leds[2], (self.estado >> 1) & 1) # LED3 (Bit 1)
        GPIO.output(self.leds[1], (self.estado >> 2) & 1) # LED2 (Bit 2)
        GPIO.output(self.leds[0], (self.estado >> 3) & 1) # LED1 (Bit 3 - el de la izquierda)

    def incrementar(self):
        self.estado += 1
        if self.estado > 15:
            self.estado = 0
        self.mostrar_consola()
        self.actualizar_leds()
        time.sleep(0.3) # Antirrebote

    def decrementar(self):
        if self.estado > 0:
            self.estado -= 1
        self.mostrar_consola()
        self.actualizar_leds()
        time.sleep(0.3) # Antirrebote

    def ejecutar(self):
        """Bucle principal que revisa los botones."""
        if GPIO.input(self.btn_inc) == GPIO.LOW:
            self.incrementar()
        if GPIO.input(self.btn_dec) == GPIO.LOW:
            self.decrementar()

# --- Ejecución del Programa ---
if __name__ == "__main__":
    # Definimos los pines: [led1, led2, led3, led4], boton_incrementar, boton_decrementar
    pines_de_leds = [17, 27, 22, 23]
    mi_contador = ContadorBinario(pines_de_leds, 24, 25)

    try:
        while True:
            mi_contador.ejecutar()
            time.sleep(0.01) # Pequeña pausa para no saturar el procesador
    except KeyboardInterrupt:
    finally:
        GPIO.cleanup() # Limpia los pines al salir
