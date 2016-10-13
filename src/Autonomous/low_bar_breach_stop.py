'''
Created on Oct 5, 2016

@author: Kenny
'''

from robotpy_ext.autonomous import StatefulAutonomous, timed_state

class Low_Bar_Breach_Stop(StatefulAutonomous):
    '''
    classdocs
    '''
    
    MODE_NAME = "Low Bar Breach Stop"

    def initialize(self):
        self.kP = self.prefs.get("kP", 0.03)
    
    @timed_state(duration=3, first=True, next_state='stop')
    def go_forward(self):
        self.left.set(1, self.gyro, self.kP)
        self.right.set(1, self.gyro, self.kP)
        
    @timed_state(duration=1, next_state='go_backward')
    def stop(self):
        self.left.set(0)
        self.right.set(0)
        
    @timed_state(duration=3, next_state='stop2')
    def go_backward(self):
        self.left.set(-1, self.gyro, self.kP)
        self.right.set(-1, self.gyro, self.kP)
        
    @timed_state(duration=1, next_state='go_forward2')
    def stop2(self):
        self.left.set(0)
        self.right.set(0)
    
    @timed_state(duration=3, next_state='end')
    def go_forward2(self):
        self.left.set(1, self.gyro, self.kP)
        self.right.set(1, self.gyro, self.kP)
        
    @timed_state(duration=1)
    def end(self):
        self.left.set(0)
        self.right.set(0)
        
    