import matplotlib.pyplot as plt
import pyspeedtest
import psutil

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