import smbus
import time
from sgp30 import SGP30

#i2c bus #1 (#0 is only used for IDing on the pi)
bus = smbus.SMBus(1)

#SI7021 address
temperatureAddress = 0x40
humidityAddress = 0x40

#SGP30 address
airQualityAddress = 0x58

def readHumidity():
    #Read 2 bytes from humidity register and sleep
    rh = bus.read_i2c_block_data(humidityAddress, 0xE3, 2)
    time.sleep(0.1)

    # Convert the data into relative humidity percentage
    humidity = ((rh[0] * 256 + rh[1]) * 125 / 65536.0) - 6
    return humidity

def readTemperature():
    #Read 2 bytes fromt temperature register and sleep
    temp = bus.read_i2c_block_data(temperatureAddress, 0xE0, 2)
    time.sleep(0.1)

    # Convert to Celsius and Fahrenheit temperatures
    cTemp = ((temp[0] * 256 + temp[1]) * 175.72 / 65536.0) - 46.85
    fTemp = cTemp * 1.8 + 32
    return fTemp

#Returns tuple with timestamp, eCO2 value, TVOC value
def readAirQuality():
    with SGP30(bus) as chip:
        return chip.measure_air_quality()

def testSensors():
    temperature = readTemperature()
    humidity = readHumidity()
    airQuality = readAirQuality()
    print ("Relative Humidity: " + str(humidity))
    print ("Temperature Fahrenheit: " + str(temperature))
    print ("eCO2: " + str(airQuality[1]))
    print ("TVOC: " + str(airQuality[2]))