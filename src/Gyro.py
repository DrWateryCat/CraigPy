'''
Created on Oct 13, 2016

@author: Kenny
'''

import wpilib
import warnings

class Gyro(object):
    def __init__(self):
        self.i2c = wpilib.I2C(wpilib.I2C.Port.kOnboard, 0x69)
        self.x = 0
        self.y = 0
        self.z = 0
        
    def enable(self):
        self.i2c.write(0x20, 0x4f)
    def disable(self):
        self.i2c.write(0x20, 0xb7)
        
    def recieve_data(self):
        xbufferl = (self.i2c.read(0x28, 1) if not wpilib.hal.HALIsSimulation() else 0) 
        xbufferh = (self.i2c.read(0x29, 1) if not wpilib.hal.HALIsSimulation() else 0)
        ybufferl = (self.i2c.read(0x2a, 1) if not wpilib.hal.HALIsSimulation() else 0)
        ybufferh = (self.i2c.read(0x2b, 1) if not wpilib.hal.HALIsSimulation() else 0)
        zbufferl = (self.i2c.read(0x2c, 1) if not wpilib.hal.HALIsSimulation() else 0)
        zbufferh = (self.i2c.read(0x2d, 1) if not wpilib.hal.HALIsSimulation() else 0)
            
        
        self.x = ((xbufferh[0] & 0xff) << 8 | (xbufferl[0] & 0xff))
        if self.x >= 32768:
            self.x -= 65536
            
        self.y = ((ybufferh[0] & 0xff) << 8 | (ybufferl[0] & 0xff))
        if self.y >= 32768:
            self.y -= 65536
        
        self.z = ((zbufferh[0] & 0xff) << 8 | (zbufferl[0] & 0xff))
        if self.z >= 32768:
            self.z -= 32768
            
    def connected(self):
        detected = (self.i2c.read(0x0F, 1) if not wpilib.hal.HALIsSimulation() else False)
        
        return detected
        
        
    def update(self):
        if self.connected():
            self.recieve_data()
            wpilib.SmartDashboard.putNumber("Gyro X", self.x)
            wpilib.SmartDashboard.putNumber("Gyro Y", self.y)
            wpilib.SmartDashboard.putNumber("Gyro Z", self.z)
        else:
            warnings.warn("No I2C detected")