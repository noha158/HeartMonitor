# HeartMonitor

This is a project for My Embedded systems class.

I used the ECG sensor to measure a heartbeat and the STM32F103C8 board to read the analog signal from the sensor and convert it into a digital signal using the on-chip ADC and then send that data to my PC to be plotted.

I used STM32CubeMX, Keil uVision5, and python (developed on PyCharm) to create this project.

This repo includes a report that contains detailed descriptions of the code and a presentation that has an overall view of the project. 

This repo has the Keil uVision project that I programmed to my board and the PyCharm project where I developed my python UI.

I used python to create a simple UI that reads the data transmitted over the UART from the USB serial port and plot that data through commands provided to the UI.

When you run the python file, the first command prompted will be to input the com port, followed by inputting the baud rate. you could then input the command which can either be "start" or "bpm". 

If your input is "start" then you will be prompted to input the sampling rate and the period for which you want you program to run, the period must be entered in seconds. below is a screenshot showing the flow of the input and the output plot:


If your input is "bpm", then the bpm value will be displayed. If you didn't run start before running bpm, then the bpm value will be none.
/Users/noha/Desktop/Screen Shot 2020-05-27 at 10.23.21 PM.png
