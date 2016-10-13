#!/usr/bin/env python3

import wpilib
import Gearbox
import Intake
import Gyro

from robotpy_ext.autonomous import AutonomousModeSelector

class MyRobot(wpilib.IterativeRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.timer = wpilib.Timer()
        
        self.gyro = Gyro.Gyro()
        
        if not wpilib.hal.HALIsSimulation():
            self.prefs = wpilib.Preferences.getInstance()
        else:
            self.prefs = None
        
        self.leftGearbox = Gearbox.Gearbox([0, 1, 2], inverted=True)
        self.rightGearbox = Gearbox.Gearbox([3, 4, 5])
        
        self.intake = Intake.Intake()
        
        self.leftJoystick = wpilib.Joystick(0)
        self.rightJoystick = wpilib.Joystick(1)
        
        self.leftGearbox.max = self.prefs.get("MaxLeftSpeed", 1)
        self.rightGearbox.max = self.prefs.get("MaxRightSpeed", 1)
        
        self.prefs.put("Robot", "CraigPy")
        
        self.components = {
                           'left':  self.leftGearbox,
                           'right': self.rightGearbox,
                           'intake': self.intake,
                           'gyro': self.gyro,
                           'prefs': self.prefs
        }
        
        self.autonomous = AutonomousModeSelector('Autonomous', self.components)
        
        

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        self.gyro.update()
        self.autonomous.run()
        
    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        
        self.gyro.update()
        
        leftSide = self.leftJoystick.getRawAxis(1)
        rightSide = self.rightJoystick.getRawAxis(1)
        
        self.leftGearbox.max = self.prefs.get("MaxLeftSpeed", 1)
        self.rightGearbox.max = self.prefs.get("MaxRightSpeed", 1)
        
        
        self.leftGearbox.set(-leftSide)
        self.rightGearbox.set(-rightSide)
        
        if self.leftJoystick.getRawButton(3) or self.rightJoystick.getRawButton(3):
            self.intake.set(-1)
        elif self.leftJoystick.getRawButton(1) or self.rightJoystick.getRawButton(1):
            self.intake.set(1)
        else:
            self.intake.set(0)
            
        

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        pass
    
    def clamp(self, minV, maxV, value):
        return max(minV, min(maxV, value))

if __name__ == "__main__":
    wpilib.run(MyRobot)
