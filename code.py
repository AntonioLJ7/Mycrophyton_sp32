import board
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import adafruit_bme680

i2c = board.I2C()  # uses board.SCL and board.SDA
i2c.try_lock()
address_lcd = i2c.scan()[0]
address_bme680 = i2c.scan()[1]
i2c.unlock()
lcd = LCD(I2CPCF8574Interface(i2c, address_lcd), num_rows=4, num_cols=20)
lcd.clear()


bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, address_bme680)
bme680.sea_level_pressure = 1013.25
temperature_offset = -5

while True:

    temp = bme680.temperature + temperature_offset
    gas = bme680.gas
    humedad = bme680.relative_humidity
    presion = bme680.pressure
    print("Pressure: %0.3f hPa" % bme680.pressure)

    print("\nTemperature: %0.1f C" % temp)
    print("Gas: %d ohm" % gas)
    print("Humidity: %0.1f %%" % humedad)
    lcd_temperatura = "Temperatura: " + str(int(temp)) + " C   "
    lcd_gas = "Gas: " + str(gas) + " ohm     "
    lcd_humedad = " Humedad: " + str(int(humedad)) + " %       "
    lcd_presion = "Presion: " + str(int(presion)) + " hPa"

    message = lcd_temperatura + lcd_gas + lcd_humedad + lcd_presion

    lcd.print(message)

    time.sleep(5)

    lcd.clear()
