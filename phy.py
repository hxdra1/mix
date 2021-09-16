import RPi.GPIO as GPIO
import time

#test a

led_pin = 27
taster_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(taster_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

class LED:
    def __init__(self, led_gpio):
        self.led_gpio = led_gpio
        
    def an(self):
        GPIO.output(self.led_gpio, True)
    
    def aus(self):
        GPIO.output(self.led_gpio, False)
    
    def status(self):
        if GPIO.output(self.led_gpio, True):
            return True
        
        elif GPIO.OUTPUT(self.led_gpio, False):
            return False
    
class Taster:
    def __init__(self, taster_gpio):
        self.taster_gpio = taster_gpio
        
    def status(self):
        if GPIO.input(self.taster_gpio) == 1:
            return True
        
        elif GPIO.input(self.taster_gpio) == 0:
            return False


    
led = LED(led_pin)
taster = Taster(taster_pin)


counter = 0
hold = 0


try:
    while True:
        if taster.status() == True:
            hold += 1
            print (hold)

    
        if taster.status() == False and hold > 1 and hold < 10000:
            counter += 1
            hold = 0
            
            if counter == 1:
                led.an()
                time.sleep(0.02)
                hold = 0
                
            if counter == 2:
                counter = 0
                led.aus()
                time.sleep(0.02)
                
        if taster.status() == False and hold > 20000:
            hold = 0
            

        
except KeyboardInterrupt:
    led.aus()
    GPIO.cleanup()
