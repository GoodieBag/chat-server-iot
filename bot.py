from motor_driver import Motor
import time


class Bot:
    """
    A class used to represent a bot with two DC motors

    Attributes
    ----------
    NA

    Methods
    -------
    move_forward()
        moves the Bot in forward direction

    move_backward()
        moves the Bot in backward direction

    turn_left()
        turns the Bot left

    turn_right()
        turns the Bot right

    stop()
        stops the Bot
    """

    def __init__(self):
        """Function to init two motors used by the Bot"""

        self.motor1 = Motor(12, 11)
        self.motor2 = Motor(15, 16)

    def move_forward(self):
        """Function to move bot in forward direction"""

        self.motor1.turn_clockwise()
        self.motor2.turn_clockwise()
        time.sleep(1)
        self.stop()

    def move_backward(self):
        """Function to move bot in backward direction"""

        self.motor1.turn_anticlockwise()
        self.motor2.turn_anticlockwise()
        time.sleep(1)
        self.stop()

    def turn_left(self):
        """Function to turn bot left"""

        self.motor1.turn_anticlockwise()
        self.motor2.turn_clockwise()
        time.sleep(1)
        self.stop()

    def turn_right(self):
        """Function to turn bot right"""

        self.motor1.turn_clockwise()
        self.motor2.turn_anticlockwise()
        time.sleep(1)
        self.stop()

    def stop(self):
        """Function to stop bot"""

        self.motor1.stop()
        self.motor2.stop()
