#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
"""

import wpilib
import wpilib.drive
from state import state
from oi import read_input



class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.left_motor = wpilib.Spark(0)
        self.right_motor = wpilib.Spark(1)
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)

        self.lift_motor1 = wpilib.Spark(2)
        self.lift_motor2 = wpilib.Spark(3)
        
        self.claw_motor1 = wpilib.Spark(4)
        self.claw_motor2 = wpilib.Spark(5)

        self.stick = wpilib.Joystick(1)
        self.timer = wpilib.Timer()


    def teleopPeriodic(self):

        read_input()
        """This function is called periodically during operator control."""
        x = state["Chasis_x_mov"]
        y = state["Chasis_y_mov"]

        self.drive.arcadeDrive(y,x)

    

        if state["NIVEL1"]:
            state["auto_timer"] += 1

                    
            if state["auto_timer"] <= 100: 

                self.lift_motor1.set(0.5)
                self.lift_motor2.set(0.5)
              
            elif state["auto_timer"] <= 150: 
            
                self.lift_motor1.set(0)
                self.lift_motor2.set(0)
                self.claw_motor1.set(0.5)
                self.claw_motor2.set(0.5)
           
                    
            elif state["auto_timer"] <= 200:
                self.claw_motor1.set(0)
                self.claw_motor2.set(0)
                self.claw_motor1.set(-0.5)
                self.claw_motor2.set(-0.5)
                
                    
            elif state["auto_timer"] <= 250: 
                self.claw_motor1.set(0)
                self.claw_motor2.set(0)
                self.lift_motor1.set(-0.5)
                self.lift_motor2.set(-0.5)    
               
   
            else:
                self.claw_motor1.set(0)
                self.claw_motor2.set(0)
                self.lift_motor1.set(0)
                self.lift_motor2.set(0)




        elif state["NIVEL2"]:
            state["auto_timer"] += 1
            
            if state["auto_timer"] <= 100: 

                self.lift_motor1.set(0.5)
                self.lift_motor2.set(0.5)     
               

            elif state["auto_timer"] <= 250: 
                self.lift_motor1.set(0)
                self.lift_motor2.set(0)
                self.claw_motor1.set(0.5)
                self.claw_motor2.set(0.5)    
       
                    
            elif state["auto_timer"] <= 300: 
                self.claw_motor1.set(0)
                self.claw_motor2.set(0)
                self.claw_motor1.set(-0.5)
                self.claw_motor2.set(-0.5)
       
                    
            elif state["auto_timer"] <= 450: 
                self.claw_motor1.set(0)
                self.claw_motor2.set(0)
                self.lift_motor1.set(-0.5)
                self.lift_motor2.set(-0.5)    
      

   
            else:
                self.claw_motor1.set(0)
                self.claw_motor2.set(0)
                self.lift_motor1.set(0)
                self.lift_motor2.set(0)



        elif state["NIVEL3"]:

            state["auto_timer"] += 1
            
                    
            if state["auto_timer"] <= 100: 
                self.lift_motor1.set(0.5)
                self.lift_motor2.set(0.5)     
                
            elif state["auto_timer"] <= 350: 
                self.lift_motor1.set(0)
                self.lift_motor2.set(0)
                self.claw_motor1.set(0.5)
                self.claw_motor2.set(0.5)    
           
                    
            elif state["auto_timer"] <= 400: 
                self.claw_motor1.set(0)
                self.claw_motor2.set(0)
                self.claw_motor1.set(-0.5)
                self.claw_motor2.set(-0.5)
              
                    
            elif state["auto_timer"] <= 650: 
                self.claw_motor1.set(0)
                self.claw_motor2.set(0)
                self.lift_motor1.set(-0.5)
                self.lift_motor2.set(-0.5)    
               
   
            else:
                self.claw_motor1.set(0)
                self.claw_motor2.set(0)
                self.lift_motor1.set(0)
                self.lift_motor2.set(0)
        else:

            state["auto_timer"] = 0





if __name__ == "__main__":
    wpilib.run(MyRobot)