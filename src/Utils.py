'''
Created on Oct 4, 2016

@author: Kenny
'''

import math

def clamp(minV, maxV, value):
    return max(minV, min(maxV, value))

def drive(magnitude, curve, gyro, kP=0.03):
    
    curve *= -(gyro.y * kP)
    
    if curve < 0:
        value = math.log(-curve)
        ratio = (value - 0.5) / (value + 0.5)
        if ratio == 0:
            ratio = .0000000001
        leftOutput = magnitude / ratio
        rightOutput = magnitude
    elif curve > 0:
        value = math.log(curve)
        ratio = (value - 0.5) / (value + 0.5)
        if ratio == 0:
            ratio = .0000000001
        leftOutput = magnitude
        rightOutput = magnitude / ratio
    else:
        leftOutput = magnitude
        rightOutput = magnitude
        
    return [leftOutput, rightOutput]

def autodrive(leftMotor, rightMotor, magnitude, curve, gyro):
    speeds = drive(-magnitude, curve, gyro)
    
    leftMotor.set(speeds[0])
    rightMotor.set(speeds[1])