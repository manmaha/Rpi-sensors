#Test sensors

import time
import board
import busio
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306, adafruit_vl53l0x, adafruit_mpu6050,adafruit_ahtx0

WIDTH = 128
HEIGHT = 32  # Change to 64 if needed
BORDER = 5



i2c = i2c = busio.I2C(board.SCL, board.SDA)

try:
	oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3c)
except :
	oled = None
	print('Could not set up Oled')

try :
	mpu = adafruit_mpu6050.MPU6050(i2c)
except:
	mpu = None
	print('Could not set up MPU')

try : 
	aht21  = adafruit_ahtx0.AHTx0(i2c)
except:
	aht21 = None
	print('Could not set up temperature sensor') 

try : 
	vl53 = adafruit_vl53l0x.VL53L0X(i2c)
except:
	vl53 = None
	print('Could not set up TOF sensor')

while True:
	if aht21 :
		print('AHT 21 Temperature {:0.2f} C'.format(aht21.temperature))
	if vl53 :
		print('Distance {} mm'.format(vl53.range))
	if mpu :
		print('MPU Temperature {:0.2f} C'.format(mpu.temperature))

	time.sleep(3)





