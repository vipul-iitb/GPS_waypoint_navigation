import serial
import time
from math import*
import future

lat1 = input("Enter latitude of destination")
lon1 = input("enter longitude of destination")

SerialData = serial.Serial('com7',115200)

def haversine(lat1,lon1,lat2,lon2):
	lat1 = radians(lat1)
	lat2 = radians(lat2)
	lon2 = radians(lon2)
	lon1 = radians(lon1)
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*(sin(dlon/2))**2
	c = 2*atan2(sqrt(a),sqrt(1-a))
	r = 6371
	d = r*c
	return d

def bearing(lat1,lon1,lat2,lon2,comp):
	lat1 = radians(lat1)
	lat2 = radians(lat2)
	lon2 = radians(lon2)
	lon1 = radians(lon1)
	dlon = lon2 - lon1
	dlat = dlat = lat2 - lat1
	y = sin(dlon)*cos(lat2)
	x = cos(lat1)*sin(lat2) - sin(lat1)*cos(lat2)*cos(dlon)
	bearing = atan2(y,x)
	bearing = (degrees(bearing) + 360) % 360
	bearing = bearing - comp
	bearing = (bearing + 360)%360
	return bearing

while(1):
	try:
		if(SerialData.inWaiting > 0):
			myData = SerialData.readline()
			if(myData.startswith("*") or myData.startswith("|")):
				continue
			lst = myData.split("|")
			lat = float(lst[0])
			lon = float(lst[1])
			comp = float(lst[2])
                        dist = haversine(lat1,lon1,lat,lon)
                        dist = dist*1000
			bear = bearing(lat,lon,lat1,lon1,comp)
			print (dist)
                        print (bear)
	except:
		print("wait for 5 seconds, error with sensor data")
		time.sleep(5)
		pass
