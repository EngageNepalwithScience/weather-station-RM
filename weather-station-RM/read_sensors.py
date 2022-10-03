import numpy as np
import bme280_sensor as air_temp
import ds18b20_therm as ground_temp
import mh_z19.mh_z19 as co2_sensor

def get_temperature_measurements():
    print("Engage Nepal with Science")
    print("Weather station V1.0\n")
    print("Please be sure to note today's date, and the current time.\n")
    
    # If the sensor is available, we measure the ground temperature from DS18B20
    try:
        g_temp_obj = ground_temp.DS18B20()
        g_temp = g_temp_obj.read_temp()
    except:
        g_temp = 0
    if g_temp != 0:
        print("\tAcquiring data from ground sensor.")
        print("\t\tGround temperature is %0.2f degrees celsius.\n" %g_temp)
    
    # air temperature from BME280
    print("\tAcquiring data from air sensor, please wait.")
    bme_temp, bme_hum, bme_pres = air_temp.readBME()
    print("\t\tAir temperature is %0.2f degrees celsius." %bme_temp)
    print("\t\tRelative humidity is %0.2f%%." %bme_hum)
    print("\t\tAbsolute barometric pressure is %0.2f millibars.\n" %bme_pres)
    #print(bme_temp, bme_hum, bme_pres)
    
def get_co2():
    print("\tAcquiring data from CO2 sensor.")
    co2_val = co2_sensor.read()['co2']
    print("\t\tCO2 concentration right now is %d ppm." %co2_val)

get_temperature_measurements()
get_co2()

print("Thank you.")
