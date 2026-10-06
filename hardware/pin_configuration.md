# Raspberry Pi Pin Configuration

## RC522
SDA/SS -> GPIO8 (pin 24)
SCK -> GPIO11 (pin 23)
MOSI -> GPIO10 (pin 19)
MISO -> GPIO9 (pin 21)
RST -> GPIO25 (pin 22)
3.3V -> pin 1
GND -> pin 6

## LCD I2C
SDA -> GPIO2 (pin 3)
SCL -> GPIO3 (pin 5)
VCC -> 5V (pin 2)
GND -> pin 6

## Servos
Servo 1 signal -> GPIO17 (pin 11)
Servo 2 signal -> GPIO27 (pin 13)
Servo power -> regulated external 5V
Servo ground and Raspberry Pi ground must be common.

IMPORTANT: RC522 is a 3.3V device. Do not connect its power to 5V.
