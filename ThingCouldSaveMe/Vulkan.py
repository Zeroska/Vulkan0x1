#!/bin/python3 
#This is Vulkan, Vulkan is a tool that allow you to calculate the IP addresses,
#Class and help you do subnetting this is a tool I code for the Hoa Sen University Student who are struggle in subnetting
#The Documention will come soon 

import sys


#craft the UserInput when you enter an network ID (like 192.168.1.0) it will calculate to know which class the ip address in 
#like class A,B or C 


def takeUserInput(theIpAddress): #the ip address is a string 
    #the ip address had 4 part x.x.x.x each x range from 1 to 255, so you need to 
    for i in range(len(theIpAddress)):
        
