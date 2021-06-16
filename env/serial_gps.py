import serial

def normAngle(x):
    result = x
    if x <= -180:
        result = x + 360
    if x > 180: 
        result = x - 360
    
    return result

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

from skyfield.api import N, W, load, wgs84
planets = load('de440s.bsp')  # ephemeris DE421

ts = load.timescale()
t = ts.now()

with serial.Serial('/dev/ttyACM0', baudrate=4800, timeout=1) as ser:
    line = ser.readline()
    str_line=str(line)
    print(str_line)
    while "GPRMC" not in str_line:
        line=ser.readline()
        str_line=str(line)
        print(str_line)

    split_line=str_line.split(',')
    lat = split_line[3] + " * " + split_line[4]
    long = split_line[5] + " * " + split_line[6]
split_lat=lat.split('.')
lat_degree = int(split_lat[0][:-2])
lat_minutes = str(float(lat[-12:-4])/60)
lat_minutes = lat_minutes[:7]
lat_direction = split_lat[1][-1:]
if(lat_direction=="S"):
    lat_direction_int = -1
else:
    lat_direction_int = 1
lat_format = (lat_degree + float(lat_minutes))*lat_direction_int
split_long=long.split('.')
long_degree = int(split_long[0][:-2])
long_minutes = str(float(long[-12:-4])/60)
long_minutes = long_minutes[:7]
long_direction = split_long[1][-1:]
if(long_direction=="W"):
    long_direction_int = -1
else:
    long_directioin_int = 1
long_format = (long_degree + float(long_minutes))*long_direction_int
sun, earth = planets['Sun'], planets['Earth']
#print("Sun values:", sun)

print(lat_format, long_format) #39.88384 -84.1236
tracker = earth + wgs84.latlon(lat_format, long_format)
astrometric = tracker.at(t).observe(sun)
alt, az, d = astrometric.apparent().altaz()
alt = float(str(alt).split('deg')[0])
az = float(str(az).split('deg')[0])
alt = normAngle(alt);
az = normAngle(az);
print("Position from local horizon: ", alt)
print("Direction from North Pole: ", az)

#kit.servo[0].angle = az
#kit.servo[3].angle =  alt 90 is straight up, 180 is at horizon