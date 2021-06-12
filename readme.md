http://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c

linux
source env/bin/activate

sudo apt-get install python-smbus
sudo apt-get install i2c-tools

stty -F /dev/ttyACM0 ispeed 4800 && cat </dev/ttyACM0


planets = load('de421.bsp')  # ephemeris DE421

pip freeze > requirements.txt

https://rhodesmill.org/skyfield/toc.html