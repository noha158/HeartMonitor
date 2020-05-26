import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import serial

x_len = 200
y_range = [0, 4096]

def serialRead(samplingRate):
    bpm = ser.readline().decode('utf-8')
    while bpm.find('B') == -1:
        bpm = ser.readline().decode('utf-8')
        bpm = bpm.strip("\n")
        bpm = bpm.strip("\r")
    return bpm
# This function is called periodically from FuncAnimation

def inti_func():
    plt.title('Heart Rate Monitor')
    plt.xlabel('Samples')
    plt.ylabel('ECG Output')

def animate(i,ys,samplingRate):
    global bpmFinal
    print("in animate")
    line = ser.readline().decode('utf-8')
    line = line.strip("\n")
    line = line.strip("\r")
    print("val = ", str(line))
    if(line.find('B') != -1):
        print("time ended")
        ys.clear()
        ys = [0] * x_len
        bpmFinal = line
        ani.event_source.stop()
    if((len(line) > 0) and (len(line) < 5) and (line.find('\r')==-1)):
        line = float(line)
        ys.append(line)
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
    samplingRate = input("Enter the Sampling rate: ")
    if ser.is_open is not True:
        ser.open()
    bpm = ""
    call = 0
    while True:
        command = input("Enter your command: ")
        samplingRate2 = samplingRate + "\r"
        if(command == "start"):
            print("in")
            call = call + 1
            ser.write(samplingRate2.encode())
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            xs = list(range(0, 200))
            ys = [0] * x_len
            ax.set_ylim(y_range)
            line2, = ax.plot(xs, ys)
            ani = animation.FuncAnimation(fig, animate, init_func=inti_func, repeat=True, fargs=(ys, samplingRate), interval=1, save_count=200)
            print("why")
            plt.show()
        elif (command == "bpm"):
            print(bpmFinal)
