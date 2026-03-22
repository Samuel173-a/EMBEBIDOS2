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


    // CONFIGURACIÓN DEL RELOJ: Indispensable para la TM4C1294XL
    // Establece la frecuencia a 120 MHz 
    SysCtlClockFreqSet((SYSCTL_XTAL_25MHZ | SYSCTL_OSC_MAIN | 
                        SYSCTL_USE_PLL | SYSCTL_CFG_VCO_480), 120000000);

    // Habilitar el puerto N [cite: 148, 154]
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPION);
    while(!SysCtlPeripheralReady(SYSCTL_PERIPH_GPION)) { } 

    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOJ);
    while(!SysCtlPeripheralReady(SYSCTL_PERIPH_GPIOJ)) { } 
    
    // Configurar pines 0 y 1 como salida [cite: 162, 193]
    GPIOPinTypeGPIOOutput(GPIO_PORTN_BASE, 0x02);
    
    GPIOPinTypeGPIOInput(GPIO_PORTJ_BASE, GPIO_PIN_1);
    GPIOPadConfigSet(GPIO_PORTJ_BASE, GPIO_PIN_1, GPIO_STRENGTH_2MA, GPIO_PIN_TYPE_STD_WPU);

    while(1) {
        if(GPIOPinRead(GPIO_PORTJ_BASE, GPIO_PIN_1) == 0) {
            GPIOPinWrite(GPIO_PORTN_BASE, 0x02, 0x02);

        }
        else{
        // Apagar ambos LEDs [cite: 183]
        GPIOPinWrite(GPIO_PORTN_BASE, 0x02, 0x0);

        }
        
    }
}