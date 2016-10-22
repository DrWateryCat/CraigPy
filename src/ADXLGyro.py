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
        
        self.yavg = [0] * 50
        
        self.i = 0
        
        self.gyro = wpilib.AnalogGyro(0)
        
        
    def calibrate(self):
        self.gyro.calibrate()
        
    def update(self):
        angle = self.gyro.getAngle()
        
        self.yavg[self.i] = angle
        
        self.i += 1
        if self.i > 49:
            self.gyro.reset()
            self.i = 0
            
            avg = 0
            for x in self.yavg:
                avg += x
            avg /= len(self.yavg)
            
            self.y = avg
        
    def reset(self):
        self.gyro.reset()
        self.y = 0
        
    def enable(self):
        pass