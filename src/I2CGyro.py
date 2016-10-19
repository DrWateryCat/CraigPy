'''
Created on Oct 13, 2016

@author: Kenny
'''

import wpilib
import warnings
from _ast import Num

class Gyro(object):
    def __init__(self):
        self.i2c = wpilib.I2C(wpilib.I2C.Port.kOnboard, 0x69)
        self.x = 0
        self.y = 0
        self.z = 0
        
        self.xbuf = [0] * 50
        self.ybuf = [0] * 50
        self.zbuf = [0] * 50
        
        self.i = 0
        
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
            
        
        self.xa = ((xbufferh[0] & 0xff) << 8 | (xbufferl[0] & 0xff))
        if self.xa >= 32768:
            self.xa -= 65536
            
        self.ya = ((ybufferh[0] & 0xff) << 8 | (ybufferl[0] & 0xff))
        if self.ya >= 32768:
            self.ya -= 65536
        
        self.za = ((zbufferh[0] & 0xff) << 8 | (zbufferl[0] & 0xff))
        if self.za >= 32768:
            self.za -= 32768
            
        self.xbuf[self.i] = self.xa
        self.ybuf[self.i] = self.ya
        self.zbuf[self.i] = self.za    
        
        self.i += 1
        if self.i > 49:
            self.i = 0
            
            xavg = 0
            for num in self.xbuf:
                xavg += num
            xavg /= 50
            
            self.x = xavg
            
            yavg = 0
            for num in self.ybuf:
                yavg += num
            yavg /= 50
            
            self.y = yavg
            
            zavg = 0
            for num in self.zbuf:
                zavg += num
            zavg /= 50
            
            self.z = zavg
            
    def connected(self):
        detected = (self.i2c.read(0x0F, 1) if not wpilib.hal.HALIsSimulation() else False)
        
        if detected is not None or detected is not False:
            return True
        else:
            return False
        
        
    def update(self):
        wpilib.SmartDashboard.putString("Gyro Connected", self.connected())
        self.recieve_data()
        
        
        