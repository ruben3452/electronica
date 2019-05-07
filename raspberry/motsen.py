import time
import RPi.GPIO as GPIO
def measure():
 # This function measures a distance
 GPIO.output(GPIO_TRIGGER, True)
 time.sleep(0.00001)
 GPIO.output(GPIO_TRIGGER, False)
 start = time.time()

 while GPIO.input(GPIO_ECHO)==0:
   start = time.time()

 while GPIO.input(GPIO_ECHO)==1:
   stop = time.time()

 elapsed = stop-start
 distance = (elapsed * 34300)/2

 return distance

GPIO.setmode(GPIO.BCM)
     
in1_pin = 24
in2_pin = 21
     
GPIO.setup(in1_pin, GPIO.OUT)
GPIO.setup(in2_pin, GPIO.OUT)
     
#def set(property, value):
 #   try:
  #      f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
   #     f.write(value)
    #    f.close()	
    #except:
     #   print("Error writing to: " + property + " value: " + value)
     
#set("delayed", "0")
#set("mode", "pwm")
#set("frequency", "500")
#set("active", "1")
     
def atras():
    GPIO.output(in1_pin, True)    
    GPIO.output(in2_pin, False)
     
def counter_clockwise():
    GPIO.output(in1_pin, False)
    GPIO.output(in2_pin, True)

def stop():
    GPIO.output(in1_pin, False)
    GPIO.output(in2_pin, False)
          
stop()


# -----------------------
# Main Script
# -----------------------

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO    = 18

print "Ultrasonic Measurement"

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
# Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)
# Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:

 while True:

     distance = measure()
     #print "Distance : %.1f" % distance
     time.sleep(0.5)
     #cmd = raw_input("Command, f/r/s 0..9, E.g. f5 :")
     #direction = cmd[0]
     if distance <= 40:
         counter_clockwise()
     else: 
         
         atras()

    # if direction == "s":
     #    stop()

except KeyboardInterrupt:
 # User pressed CTRL-C
 # Reset GPIO settings
 GPIO.cleanup()
                  

