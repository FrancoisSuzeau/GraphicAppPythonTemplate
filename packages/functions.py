import matplotlib.pyplot as plt
import pyspeedtest
import psutil
import os
import sys

def getSpeedTest():
    # Generate values
    test = pyspeedtest.SpeedTest("www.google.com")
    down = test.download()
    ping = test.ping()
    
    return down, ping

def getRAMStatistics():
    virtual_mem = psutil.virtual_memory()
    # total memory excluding swap
    total = virtual_mem[0]
    # available memory for processes
    available = virtual_mem[1]
    # memory usage in percent
    percent = virtual_mem[2]
    # the memory used
    used = virtual_mem[3]
    # memory not used at and is readily available
    free = virtual_mem[4]

    return total, available, percent, used, free

def getCPUStatistics(seconds=0):
    # Calling psutil.cpu_precent() for seconds
    return psutil.cpu_percent(seconds)

#https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)