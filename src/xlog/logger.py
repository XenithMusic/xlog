from datetime import datetime
import os,time,atexit

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

now = datetime.utcnow()
lnow = datetime.now()
start = int(now.timestamp())
directory = os.getcwd()
print("Logger begun at " + str(int(start)) + " seconds since the epoch.")
print("(local time)    " + str(int(lnow.timestamp())))
logpath = os.path.join(directory,"log",str(start)+".txt")
try:
    os.mkdir(os.path.join(directory,"log"))
except:
    print("Log directory already exists.")
file = open(logpath,"a+")
@atexit.register
def onClose():
    file.close()
    print("Successfully closed log file.")
    print("Log file can be found at " + logpath)

# Make sure the log is closed when the program exits

def format(msg,t):
    ret = "[" + now.strftime("%H:%M:%S") + "] [" + t + "] " + msg
    return

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
