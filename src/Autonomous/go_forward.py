'''
Created on Oct 4, 2016

@author: Kenny
'''

from robotpy_ext.autonomous import StatefulAutonomous, timed_state

class Go_Forward(StatefulAutonomous):
    '''
    classdocs
    '''
    
    MODE_NAME = "Go Forward"
    
    def initialize(self):
        self.kP = self.prefs.get("kP", 0.03)
    
    @timed_state(duration=1.5, first=True, next_state="stop")
    def forward(self):
        self.utils.autodrive(self.left, self.right, -1, 0, self.gyro)
               
    @timed_state(duration=12)
    def stop(self):
        self.left.set(0)
        self.right.set(0)