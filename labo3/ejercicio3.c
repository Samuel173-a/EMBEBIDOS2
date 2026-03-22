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

    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOF);
    while(!SysCtlPeripheralReady(SYSCTL_PERIPH_GPIOF)) { } 

    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOJ);
    while(!SysCtlPeripheralReady(SYSCTL_PERIPH_GPIOJ)) { } 
    
    // Configurar pines 0 y 1 como salida [cite: 162, 193]
    GPIOPinTypeGPIOOutput(GPIO_PORTN_BASE, 0x03 );
    GPIOPinTypeGPIOOutput(GPIO_PORTF_BASE, 0x11 );

    GPIOPinTypeGPIOInput(GPIO_PORTJ_BASE, GPIO_PIN_0 | GPIO_PIN_1);
    GPIOPadConfigSet(GPIO_PORTJ_BASE, GPIO_PIN_0 | GPIO_PIN_1 , GPIO_STRENGTH_2MA, GPIO_PIN_TYPE_STD_WPU);
    
    int estado = 0;
    while(1) {
        if(GPIOPinRead(GPIO_PORTJ_BASE, GPIO_PIN_0) == 0) {
            if(estado < 15) estado++;
            while(GPIOPinRead(GPIO_PORTJ_BASE, GPIO_PIN_0) == 0); // Esperar a que suelte el botón
        }

        if(GPIOPinRead(GPIO_PORTJ_BASE, GPIO_PIN_1) == 0) {
            if(estado > 0) estado--;
            while(GPIOPinRead(GPIO_PORTJ_BASE, GPIO_PIN_1) == 0); // Esperar a que suelte el botón
        
        }
        
        uint32_t valN = 0;
        if(estado & 0x01) valN |= 0x02; 
        if(estado & 0x02) valN |= 0x01; //usamos un or inclusivo 

        GPIOPinWrite(GPIO_PORTN_BASE, 0x03, valN);

        // Manejo del Puerto F (Bits 2 y 3 del contador)
        // Necesitamos mover los bits del counter a las posiciones físicas de PF4 y PF0
        uint32_t valF = 0;
        if(estado & 0x04) valF |= 0x10; // Si el bit 2 del counter está activo, prende PF4 (0x10)
        if(estado & 0x08) valF |= 0x01; // Si el bit 3 del counter está activo, prende PF0 (0x01)
        GPIOPinWrite(GPIO_PORTF_BASE, 0x11, valF);
    }
}