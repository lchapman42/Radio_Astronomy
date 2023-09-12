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

while True:
    try:
        print('\nselect baudrate')
        baudrate = 9600#int(input('> '))
        break
    except:
        print('\nInvalid baudrate')
try:
    serial_conn = serial.Serial(port, baudrate)
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
        data = serial_conn.readline()
        print(data)
        if (len(data) == good_byte_string_len):

            print(data)
            print("---")
            hour = int(data[1:3])
            minute = int(data[3:5])
            second = int(data[5:7])
            print(f"{hour}:{minute}:{second}")

            lat = float(data[9:20])
            long_ = float(data[21:33])
            alt = float(data[34:46])
            print(f"lat={lat}, long={long_}, alt={alt}")

            azm = aa.calc_azimuth(lat, long_, 36.2, -100.5)
            if (azm < 0):
                azm += 360
            print("Azimuth: ", azm)
            dist = aa.calc_distance(lat, long_, 36.2, -100.5)
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
