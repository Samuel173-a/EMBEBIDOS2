#include <stdint.h>
#include <stdbool.h>
#include "inc/hw_memmap.h"
#include "driverlib/debug.h"
#include "driverlib/gpio.h"
#include "driverlib/sysctl.h"

#ifdef DEBUG
void __error__(char *pcFilename, uint32_t ui32Line) {
    while(1);
}
#endif

int main(void) {
    volatile uint32_t ui32Loop;

    // CONFIGURACIÓN DEL RELOJ: Indispensable para la TM4C1294XL
    // Establece la frecuencia a 120 MHz 
    SysCtlClockFreqSet((SYSCTL_XTAL_25MHZ | SYSCTL_OSC_MAIN | 
                        SYSCTL_USE_PLL | SYSCTL_CFG_VCO_480), 120000000);

    // Habilitar el puerto N [cite: 148, 154]
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPION);
    while(!SysCtlPeripheralReady(SYSCTL_PERIPH_GPION)) { } 
     
    // Configurar pines 0 y 1 como salida [cite: 162, 193]
    GPIOPinTypeGPIOOutput(GPIO_PORTN_BASE, 0x01 | 0x02);
    
    while(1) {
        // Enciende PNO 
        GPIOPinWrite(GPIO_PORTN_BASE, 0x01 | 0x02, 0x01);

        // Delay aumentado para que sea visible 
        for(ui32Loop = 0; ui32Loop < 5000000; ui32Loop++) { }

        // Apagar ambos LEDs [cite: 183]
        GPIOPinWrite(GPIO_PORTN_BASE, 0x01 | 0x02, 0x01 | 0x02);
    
        for(ui32Loop = 0; ui32Loop < 5000000; ui32Loop++) { }

        GPIOPinWrite(GPIO_PORTN_BASE, 0x01 | 0x02, 0x00);

        for(ui32Loop = 0; ui32Loop < 5000000; ui32Loop++) { }
    }
}