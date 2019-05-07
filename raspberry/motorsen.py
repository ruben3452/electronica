

import RPi.GPIO as io
GPIO.setmode(GPIO.BCM)
     
in1_pin = 17
in2_pin = 18
     
GPIO..setup(in1_pin, GPIO.OUT)
GPIO.setup(in2_pin, GPIO.OUT)


GPIO_TRIGGER = 23          
GPIO_ECHO    = 24          
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  
GPIO.setup(GPIO_ECHO,GPIO.IN)      
GPIO.output(GPIO_TRIGGER,False)    
     
def set(property, value):
    try:
        f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
        f.write(value)
        f.close()	
    except:
        print("Error writing to: " + property + " value: " + value)
     
set("delayed", "0")
set("mode", "pwm")
set("frequency", "500")
set("active", "1")
     
def clockwise():
    GPIO.output(in1_pin, True)    
    GPIO.output(in2_pin, False)
     
def counter_clockwise():
    GPIO.output(in1_pin, False)
    GPIO.output(in2_pin, True)

def stop():
    GPIO.output(in1_pin, False)
    GPIO.output(in2_pin, False)
          
stop()
     
while True:
    cmd = raw_input("Command, f/r/s 0..9, E.g. f5 :")
    direction = cmd[0]
    if direction == "f":
        clockwise()
    else: 
        counter_clockwise()

    if direction == "s":
        stop()
