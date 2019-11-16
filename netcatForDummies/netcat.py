#!/urs/bin/env python3


import sys
import socket
import getopt #what is this module ??
import threading #what is this do ??
import subprocess #what is this ?


#define some global variables
#nothing so special about this until it loaded
listen      = False
command     = False
upload      = False 
execute     = ""
target      = ""
upload_destination = ""
port        = 0 #it will change when you active the damn program above 1023 
                #is non-privilede port you can you for your service 

def usage(): #for the next time



def main():
  global listen
  global command 
  global upload 
  global execute 
  global upload_destination
  global target 
  if not len(sys.argv[1]):
    usage()
  #read the command line option
  try:
    opts, args = getopt.getopt(sys.argv[1],"hle:t:p:cu:",
                    ["help","listen","execute","target","port","command","upload"])
  except getopt.GetoptError as err:
    print(str(err))
    usage()

  for o,a in opts:
    if





  
