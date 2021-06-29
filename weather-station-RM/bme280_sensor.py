import bme280
import smbus2
from time import sleep
import numpy as np

port = 1
address = 0x77
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

def readBME():
    meas_time = 2.5 # seconds
    meas_interval = 0.25 # second
    num_pts = int(meas_time/meas_interval)
    hum = np.zeros(num_pts)
    pres = np.zeros(num_pts)
    temp = np.zeros(num_pts)
    for i in range(num_pts):
        bme280_data = bme280.sample(bus, address)
        humidity  = bme280_data.humidity
        pressure  = bme280_data.pressure
        ambient_temperature = bme280_data.temperature
        # print(ambient_temperature, humidity, pressure)
        hum[i] = humidity
        pres[i] = pressure
        temp[i] = ambient_temperature
        sleep(meas_interval)

    # taking average of the above
    avg_temp = np.mean(temp)
    avg_pres = np.mean(pres)
    avg_hum = np.mean(hum)
    avg_temp = np.round(avg_temp, 2)
    avg_pres = np.round(avg_pres, 2)
    avg_hum = np.round(avg_hum, 2)
    # print("Temperature = ", avg_temp)
    # print("Humidity = ", avg_hum)
    # print("Pressure = ", avg_pres)
    return avg_temp, avg_hum, avg_pres

#temp1, hum1, pres1 = readBME()
#print(temp1, hum1, pres1)
