<div align="center">

# bot telegram on ESP32

</div>

## Requirements

- Python 3.10 or higher
- ESP32

## Optional

```
On windows:

python -m venv .env
.\env\Scripts\activate

On linux/mac:
python3 -m venv .env
source .env/bin/activate
```

## Installer

```
git clone https://github.com/watchakorn-18k/bot-telegram-on-ESP32
cd bot-telegram-on-ESP32
```

### [esptool](https://github.com/espressif/esptool)

```cmd
pip install esptool
or
pip3 install esptool

```

### [ampy](https://github.com/adafruit/ampy)

```cmd
pip install adafruit-ampy
or
pip install adafruit-ampy
```

## Download the firmware image for MicroPython or CircuitPython for your specific ESP32 board from the official website.

- https://micropython.org/download/ESP32_GENERIC/
- Download the firmware [v1.20.0 (2023-04-26) .bin](https://micropython.org/resources/firmware/ESP32_GENERIC-20230426-v1.20.0.bin)
- Save it to `FIRMWARE/esp32-20230426-v1.20.0.bin`

## Start

- Flash frimware

```
On windows:
esptool --port COM4 --baud 115200 write_flash 0x1000 FIRMWARE/esp32-20230426-v1.20.0.bin

On linux/mac:
esptool --port dev/ttyUSB0 --baud 115200 write_flash 0x1000 FIRMWARE/esp32-20230426-v1.20.0.bin
or
esptool --port dev/ttyACM0 --baud 115200 write_flash 0x1000 FIRMWARE/esp32-20230426-v1.20.0.bin

```

    On windows:

    --port COM4 you can find it at `Device Manager > Port`

    On linux/mac:
    --port dev/ttyUSB0 or --port dev/ttyACM0

- Install module to ESP32

```
pip install --user mpremote

mpremote connect COM4 mip install urequests
```

- Create a file named `main.py` for test

```main.py
import machine
import time
led_pin = machine.Pin(2, machine.Pin.OUT)
while True:
    led_pin.on()
    time.sleep(1)
    print("ON")
    led_pin.off()
    time.sleep(1)
    print("OFF")
```

- Run with local

```
ampy --port COM4 run main.py
```

- Edit in `wifi.py`

```
ssid = "YOUR_NAME_WIFI"
key = "YOUR_PASSWORD_WIFI"
```

- Edit in `main.py` with copy code from `bot_telegram.py` then change `BOT_TOKEN`

```
BOT_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

- Try to run after edited

```
ampy --port COM4 run main.py
```

- When done, upload file `main.py` to ESP32

```
ampy --port COM4 put main.py
```

<div align="center">

![image](https://cdn.discordapp.com/attachments/372372440334073859/1146641955619610726/gamedfdsf.gif)

</div>
