import serial
with serial.Serial('/dev/ttyACM0', baudrate=4800, timeout=1) as ser:
    #x = ser.read()
    #s = ser.read(10)
    line = ser.readline()
print(line)