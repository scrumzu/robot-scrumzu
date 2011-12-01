'''
Created on 15-10-2011

@author: TM
'''
import sys

def fail(msg):
   raise RuntimeError(msg)

def info(msg):
   sys.stdout.write("*INFO* %s\n" % msg)
   
def warn(msg):
   sys.stdout.write("*WARN* %s\n" % msg)