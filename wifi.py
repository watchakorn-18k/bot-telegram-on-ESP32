def conn_wifi():
    import network
    import machine
    import time
    led = machine.Pin(2, machine.Pin.OUT)
    led.on()
    ssid = "YOUR_NAME_WIFI"
    key = "YOUR_PASSWORD_WIFI"
    
    wifi = network.WLAN(network.STA_IF) 
    wifi.active(True) # activate the interface
    if not wifi.isconnected(): # check if the station is connected to an AP
        print('Connecting to network...') 
        wifi.connect(ssid, key) # connect to an AP
        while not wifi.isconnected(): # wait till we are really connected
            print('.', end='')
            time.sleep(0.1) #  you can also just put pass here
        print()
        print('Connected:', wifi.isconnected())
    else:
        print("Already connected!")
    led.off()
    print("Connected. IP address:", wifi.ifconfig()[0])
    for i in range(3):
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)