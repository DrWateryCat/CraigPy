'''
Created on Sep 30, 2016

@author: Kenny
'''

import wpilib
import Utils

class Gearbox(object):
    '''
    classdocs
    '''


    def __init__(self, motors, maxSpeed=1, inverted=False):
        '''
        Constructor
        '''
        self.motorArr = []
        self.max = maxSpeed
        self.inverted = inverted
        self.useGyro = False
        
        for motor in motors:
            self.motorArr.append(wpilib.VictorSP(motor))
            
    def set(self, value, gyro=None, kP = None):
        if gyro is not None and kP is not None:
            self.set_with_gyro(value, gyro, kP)
        else:
            enabled = True
            if not wpilib.hal.HALIsSimulation():
                prefs = wpilib.Preferences.getInstance()
                if not prefs.get('DriveEnabled', True):
                    enabled = False
                else:
                    enabled = True
            
            if enabled:
                for motor in self.motorArr:
                    if self.inverted:
                        motor.set(-Utils.clamp(-1, 1, value))
                    else:
                        motor.set(Utils.clamp(-1, 1, value))

                    
    def set_with_gyro(self, value, gyro, kP):
        enabled = True
        if not wpilib.hal.HALIsSimulation():
            prefs = wpilib.Preferences.getInstance()
            if not prefs.get('DriveEnabled', True):
                enabled = False
            else:
                enabled = True
                
        if enabled:
            for motor in self.motorArr:
                if self.inverted:
                    motor.set(-Utils.clamp(-1, 1, (value - (gyro.y * kP))))
                else:
                    motor.set(Utils.clamp(-1, 1, (value + (gyro.y * kP))))

