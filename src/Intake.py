'''
Created on Sep 30, 2016

@author: Kenny
'''

import wpilib

class Intake(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.leftMotor = wpilib.VictorSP(6)
        self.rightMotor = wpilib.VictorSP(8)
    def set(self, value):
        self.leftMotor.set(value)
        self.rightMotor.set(-value)