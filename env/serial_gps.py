import serial

from skyfield.api import N, W, load, wgs84
planets = load('de440s.bsp')  # ephemeris DE421

with serial.Serial('/dev/ttyACM0', baudrate=4800, timeout=1) as ser:
    #x = ser.read()
    #s = ser.read(10)
    line = ser.readline()
    str_line=str(line)
    split_line=str_line.split(',');
    lat = split_line[3],split_line[4]
    long =split_line[5],split_line[6]
print(split_line[3],split_line[4])
print(split_line[5],split_line[6])
print(lat)
print(long)

sun = planets['Sun']
print(sun)

tracker = earth + wgs84.latlon(lat, long)
astrometric = tracker.at(t).observe(sun)
alt, az, d = astrometric.apparent().altaz()

print(alt)
print(az)