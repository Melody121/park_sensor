import RPi.GPIO as GPIO  # Import GPIO library
import time  # Import time library

GPIO.setmode(GPIO.BCM)  # Set GPIO pin numbering

TRIG = 23  # Associate pin 23 to TRIG
ECHO = 24  # Associate pin 24 to ECHO
BEEP = 2

GPIO.setup(TRIG, GPIO.OUT)  # Set pin as GPIO out
GPIO.setup(ECHO, GPIO.IN)  # Set pin as GPIO in
GPIO.setup(BEEP, GPIO.OUT)


def GetDistance():
    GPIO.output(TRIG, False)  # Set TRIG as LOW
    time.sleep(0.1)  # Delay of 2 seconds
    GPIO.output(TRIG, True)  # Set TRIG as HIGH
    time.sleep(0.00001)  # Delay of 0.00001 seconds
    GPIO.output(TRIG, False)  # Set TRIG as LOW

    while GPIO.input(ECHO) == 0:  # Check whether the ECHO is LOW
        pulse_start = time.time()  # Saves the last known time of LOW pulse

    while GPIO.input(ECHO) == 1:  # Check whether the ECHO is HIGH
        pulse_end = time.time()  # Saves the last known time of HIGH pulse

    pulse_duration = pulse_end - pulse_start  # Get pulse duration to a variable

    distance = pulse_duration * 17150  # Multiply pulse duration by 17150 to get distance
    distance = round(distance, 2)  # Round to two decimal points

    return distance


def PlaySound(delay):
    GPIO.output(BEEP, True)
    time.sleep(delay)
    GPIO.output(BEEP, False)
    time.sleep(delay)


while True:
    distance = GetDistance()

    if distance <= 15:
        PlaySound(0.1)
    elif distance > 15 and distance <= 50:
        PlaySound(0.5)
    elif distance > 50 and distance < 100:
        PlaySound(1)

    print "Distance:", distance - 0.5, "cm"  # Print distance with 0.5 cm calibration
