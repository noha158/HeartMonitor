import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import serial

x_len = 200
y_range = [0, 4096]

def inti_func():
    plt.title('Heart Rate Monitor')
    plt.xlabel('Samples')
    plt.ylabel('ECG Output')

def readData(samplingRate):
    global bpmFinal
    ecgList = []
    stopFlag = False
    samplingRate = int(samplingRate)
    looper = int(0.25*samplingRate)
    for i in range(looper):
        line = ser.readline().decode('utf-8')
        line = line.strip("\n")
        line = line.strip("\r")
        #print("val = ", str(line))
        if(line.find('B') != -1):
            stopFlag = True
            bpmFinal = line
            return ecgList, stopFlag
        if ((len(line) > 0) and (len(line) < 5) and (line.find('\r') == -1)):
            line = float(line)
            ecgList.append(line)

    return ecgList, stopFlag


def animate(i,ys,samplingRate):
    ecgList2, stopFlag2 = readData(samplingRate)
    if(stopFlag2 == True):
        ys.clear()
        ys = [0] * x_len
        ani.event_source.stop()
    for x in ecgList2:
        ys.append(x)
    ys = ys[-x_len:]

    line2.set_ydata(ys)

    return line2,



if __name__ == '__main__':
    bpmFinal = "none"
    # initialize serial port
    ser = serial.Serial()
    counter = 0
    port = input("Enter the port number: ")
    baudrate = input("Enter the baud rate: ")
    ser.port = port
    ser.baudrate = baudrate
    if ser.is_open is not True:
        ser.open()
    bpm = ""
    call = 0
    while True:
        command = input("Enter your command: ")
        if(command == "start"):
            samplingRate = input("Enter the Sampling rate: ")
            onTime = input("Enter the sampling period: ")
            samplingRate2 = samplingRate + "\r"
            onTime2 = onTime + '\r'
            call = call + 1
            ser.write(samplingRate2.encode())
            ser.write(onTime2.encode())
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            xs = list(range(0, 200))
            ys = [0] * x_len
            ax.set_ylim(y_range)
            line2, = ax.plot(xs, ys)
            ani = animation.FuncAnimation(fig, animate, init_func=inti_func, repeat=True, fargs=(ys, samplingRate), interval=100, save_count=200)
            plt.show()
        elif (command == "bpm"):
            print(bpmFinal)
