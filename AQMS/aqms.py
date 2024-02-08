import serial

def sensor_data():
    try:
        ser = serial.Serial(port='COM5', baudrate=9600)
        print("Serial port opened successfully")
    except serial.SerialException as e:
        print("Failed to open serial port:", e)
        return None

    try:
        sensor_data_array = []
        for _ in range(9):  
            data_point = ser.readline().decode('utf-8').strip()
            sensor_data_array.append(data_point)
        
        return sensor_data_array
        
    except serial.SerialException as e:
        print("Error reading from serial port:", e)
        return None

    finally:
        ser.close()
        print("Serial port closed")

