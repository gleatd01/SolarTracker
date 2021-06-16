import serial

with serial.Serial('/dev/ttyACM0', baudrate=4800, timeout=1) as ser:
    line = ser.readline()
    str_line=str(line)
    split_line=str_line.split(',');
    lat = split_line[3],split_line[4]
    long =split_line[5],split_line[6]
print(split_line[3],split_line[4])
print(split_line[5],split_line[6])
print(lat)
print(long)

lat = "3953.02668 N";
long = "08407.41447 W";

sun = planets['Sun']
earth = planets['Earth']
print(sun)

tracker = earth + wgs84.latlon(lat, long)
astrometric = tracker.at(t).observe(sun)
alt, az, d = astrometric.apparent().altaz()

print(alt)
print(az)