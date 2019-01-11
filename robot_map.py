import wpilib

LEFT_MOTOR = wpilib.Spark(0)
RIGHT_MOTOR = wpilib.Spark(1)
DRIVE = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)