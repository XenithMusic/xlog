from datetime import datetime
import os,time

cRed    = '\033[1;31m'
cGreen  = '\033[1;32m'
cYellow = '\033[1;33m'
cBlue   = '\033[1;34m'
cPurple = '\033[1;35m'
cCyan   = '\033[1;36m'
cGray   = '\033[1;37m'
cWhite  = '\033[1;38m'
cReset  = '\033[1;0m'

dubug = "DEBUG"
info = "INFO"
warn = "WARN"
error = "ERROR"
fatal = "FATAL"

now = datetime.now()

def format(msg,t):
    return "[" + now.strftime("%H:%M:%S") + "] [" + t + "] " + msg

class logger:
    def __init__(self):
        self.log = []
    def debug(self,msg):
        m = format(msg,debug)
        print(cCyan + m + cReset)
    def info(self,msg):
        m = format(msg,info)
        print(m)
    def warn(self,msg):
        m = format(msg,warn)
        print(cYellow + m + cReset)
    def error(self,msg):
        m = format(msg,error)
        print(cRed + m + cReset)
    def fatal(self,msg):
        m = format(msg,fatal)
        print(cGray + m + cReset)
