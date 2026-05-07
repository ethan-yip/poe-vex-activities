# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Anish Batra and Ethan Yip                                                   #
# 	Created:      5/5/2026, 9:42:24 AM                                         #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain = Brain()

# -------------------------------------------- Robot Configuration --------------------------------------------
rightMotor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)  # Right drivetrain motor
leftMotor = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)  # Left drivetrain motor
# Set the leftMotor reverse property to True so that when driving forward it turns in the
# same direction as the right motor.
liftMotor = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)  # Lifearm motor
inertial_1 = Inertial(Ports.PORT5)  # Inertial sensor
bumpSwitch = Bumper(brain.three_wire_port.a)  # Bumper switch
# --------------------------------------------------------------------------------------------------------------


# -------------------------------------------- Helper Functions --------------------------------------------
def bump():
    """
    Hold the program's execution until the button is pressed
    """

    while bumpSwitch.pressing() == False:
        wait(10, MSEC)  # Debounce the button (10 ms)

        brain.screen.set_cursor(1, 1)  # Place the cursor in upper left corner of the screen
        brain.screen.print("Press the button to start the program")
        pass

    brain.screen.clear_line(1)  # Clear the text on row 1
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Program executed")
    wait(1, SECONDS)  # Wait 1 second before proceeding


def intertialCalibration():
    """
    Calibrate the inertial sensor
    A wait time of 2 seconds is required
    This function should be called at the start of the program's execution
    """

    brain.screen.clear_screen()  # Clear the brain's screen
    brain.screen.set_cursor(1, 1)  # Place the cursor in upper left corner of the screen
    brain.screen.print("Calibrating the inertial sensor")
    brain.screen.set_cursor(2, 1)  # Place the cursor on row 2
    inertial_1.calibrate()  # Calibrate the inertial sensor

    wait(2, SECONDS)  # Wait for the calibration process to complete

    brain.screen.clear_line(1)
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Inertial calibration completed")


def testInertial():
    """
    Test the inertial sensor by having it display heading and total rotation
    data. Pressing the bump switch will end the test
    """

    brain.screen.clear_screen()  # Clear the brain's screen
    while bumpSwitch.pressing() == False:
        wait(10, MSEC)  # Debounce the button (10 ms)
        brain.screen.set_cursor(5, 1)
        brain.screen.print("Heading: " + str(inertial_1.heading()))
        brain.screen.set_cursor(6, 1)
        brain.screen.print("Rotation: " + str(inertial_1.rotation()))
        brain.screen.set_cursor(8, 1)
        brain.screen.print("Press the bump switch to exit")
    brain.screen.clear_line(8)
    brain.screen.set_cursor(8, 1)
    brain.screen.print("Inertial test terminated")


def main():
    """
    The main() function is the program that will be executed by the brain
    """
    bump()  # call bump() to executed the program
    intertialCalibration()  # Calibrate the inertial sensor
    testInertial()  # Test the inertial's output


main()