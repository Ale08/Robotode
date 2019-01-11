import wpilib
from state import state
from wpilib.buttons import JoystickButton

def read_input():

	stick = wpilib.Joystick(1)
	y = stick.getY()
	state["Chasis_y_mov"] = y
	x = stick.getX()
	state["Chasis_x_mov"] = x
	A_button = stick.getRawButton(1)
	state["A_button"] = A_button
	B_button = stick.getRawButton(2)
	state["B_button"] = B_button
	X_button = stick.getRawButton(3)
	state["X_button"] = X_button
	state["NIVEL1"] = A_button
	state["NIVEL2"] = B_button
	state["NIVEL3"] = X_button



	