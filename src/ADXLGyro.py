'''
Created on Oct 17, 2016

@author: Kenny
'''

import wpilib

class ADXLGyro(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.x = 0
        self.y = 0
        self.z = 0
        
        self.gyro = wpilib.AnalogGyro(0)
        
        
    def calibrate(self):
        self.gyro.calibrate()
        
    def update(self):
        angle = self.gyro.getCenter()
        self.y = (self.gyro.getAngle() - angle)
        
    def reset(self):
        self.gyro.reset()
        self.y = 0
        
    def enable(self):
        pass