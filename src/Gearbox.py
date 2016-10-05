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


    def __init__(self, motors, maxSpeed=1):
        '''
        Constructor
        '''
        self.motorArr = []
        self.max = maxSpeed
        
        for motor in motors:
            self.motorArr.append(wpilib.VictorSP(motor))
            
    def set(self, value):
        
        #prefs = wpilib.Preferences.getInstance()
        #if prefs.get("DriveEnabled", True):
        for motor in self.motorArr:
            motor.set(Utils.clamp(-self.max, self.max, value))