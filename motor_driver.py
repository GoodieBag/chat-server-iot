import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)  # Ignore GPIO warnings

DEFAULT_PIN1 = 12
DEFAULT_PIN2 = 11


class Motor:
    """
    A class used to represent a DC motor

    Attributes
    ----------
    pin1 : int
        valid RPi GPIO pin number (DEFAULT value - 11)
    pin2 : int
        valid RPi GPIO pin number (DEFAULT value - 12)

    Methods
    -------
    turn_clockwise()
        rotates the motor in clockwise direction

    turn_anticlockwise()
        rotates the motor in anticlockwise direction

    """

    def __init__(self, pin1=DEFAULT_PIN1, pin2=DEFAULT_PIN2):
        """Function to init two pins used by the motor as output"""

        self.pin1 = pin1
        self.pin2 = pin2

        GPIO.setmode(GPIO.BOARD)  # use BOARD numbering for GPIO

        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)

    def turn_clockwise(self):
        """Function to move motor in clockwise direction"""

        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.HIGH)

    def turn_anticlockwise(self):
        """Function to move motor in anticlockwise direction"""

        GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.LOW)

    def stop(self):
        """Function to stop motor rotation"""

        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.LOW)
