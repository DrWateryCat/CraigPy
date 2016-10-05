'''
Created on Oct 4, 2016

@author: Kenny
'''
from robotpy_ext.autonomous import StatefulAutonomous, timed_state

class Do_Nothing(StatefulAutonomous):
    '''
    classdocs
    '''
    
    MODE_NAME = "Do Nothing"
    DEFAULT = True
    
    def initialize(self):
        pass
    @timed_state(duration=15, first=True)
    def do_nothing(self):
        pass
        