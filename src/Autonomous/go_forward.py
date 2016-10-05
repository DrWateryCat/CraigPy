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
        pass
    
    @timed_state(duration=3, first=True, next_state="stop")
    def forward(self):
        self.left.set(1)
        self.right.set(1)
        
    @timed_state(duration=12)
    def stop(self):
        self.left.set(0)
        self.right.set(0)