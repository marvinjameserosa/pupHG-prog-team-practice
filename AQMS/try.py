import serial

try:
    ser = serial.Serial(port='COM5', baudrate=9600)
    print("Serial port opened successfully")
except serial.SerialException as e:
    print("Failed to open serial port:", e)
    exit()

try:
    while True:
        value = ser.readline()
        valueInStr = value.decode('utf-8').strip()
        print(valueInStr)
except KeyboardInterrupt:
    print("Serial communication stopped by user")
finally:
    ser.close()
    print("Serial port closed")