from time import sleep
import serial
import serial.tools.list_ports
import azimuth_altitude_gps as aa

def search_for_ports():
    ports = list(serial.tools.list_ports.comports())
    return ports

print('''
    Azimuth Angle:
    \tN\t\t
    \t|\t\t
    \t|\t\t
    \tP1 --- P2\n''')

print('available ports')
for index, port in enumerate(search_for_ports()):
    print('[{}] {}'.format(index, port.description))

print('\nselect port to connect P1 to (use index number)')

while True:
    try:
        ser_device = int(input('> '))
        port = search_for_ports()[ser_device].device
        break
    except Exception as error:
        print(error)
        print('Invalid port')

print('\nselect port to connect P2 to (use index number)')

while True:
    try:
        ser_device2 = int(input('> '))
        port2 = search_for_ports()[ser_device].device
        if (ser_device2 == ser_device):
            raise Exception("P2 device cannot connected to the same port as P1 device")
        break
    except Exception as error:
        print(error)
        print('Invalid port')

while True:
    try:
        print('\nselect baudrate (Default to 9600)')
        baudrate = 9600#int(input('> '))
        break
    except:
        print('\nInvalid baudrate')
try:
    serial_conn = serial.Serial(port, baudrate)
except:
    print('\nCant connect to port {}'.format(port))
    exit(0)

try:
    serial_conn2 = serial.Serial(port2, baudrate)
except:
    print('\nCant connect to port {}'.format(port))
    exit(0)

count = 0
while not serial_conn.is_open:
    sleep(0.1)
    if count == 10:
        print('\nTimed out')
        exit(0)

print('\nconnection established')

good_byte_string_len = 48

while serial_conn.is_open:
    try:
        print("---")
        data = serial_conn.readline()
        print("data:")
        print(data)
        data2 = serial_conn2.readline()
        print("data2")
        print(data2, "\n\n")
        print("---")
        if (len(data) == good_byte_string_len):

            print("\n\n")
            hour = int(data[1:3])
            minute = int(data[3:5])
            second = int(data[5:7])
            print("Time P1:")
            print(f"{hour}:{minute}:{second}")

            hour2 = int(data2[1:3])
            minute2 = int(data2[3:5])
            second2 = int(data2[5:7])
            print("Time P2:")
            print(f"{hour2}:{minute2}:{second2}")

            lat = float(data[9:20])
            long_ = float(data[21:33])
            alt = float(data[34:46])
            print("Position P1:")
            print(f"lat={lat}, long={long_}, alt={alt}")

            lat2 = float(data2[9:20])
            long_2 = float(data2[21:33])
            alt2 = float(data2[34:46])
            print("Position P2:")
            print(f"lat={lat2}, long={long_2}, alt={alt2}")
            print("\n\n")

            azm = aa.calc_azimuth(lat, long_, lat2, long_2)
            if (azm < 0):
                azm += 360
            print("Azimuth: ", azm)
            dist = aa.calc_distance(lat, long_, lat2, long_2)
            print("Distance:", dist)

            with open("my_file.txt", "ab") as binary_file:

                binary_file.write(data)

        else:
            print(f"Byte string of length {len(data)} received:")
            print(data)

    except Exception as error:
        print(error)
        break

print('\nconnection lost')
exit(0)
