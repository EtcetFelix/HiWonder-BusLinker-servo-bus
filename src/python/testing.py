from lewansoul_servo_bus import ServoBus

with ServoBus(port='COM5', baudrate=115200, timeout=1, on_enter_power_on=True) as servo_bus:
    # print(servo_bus.id_read(254))
    print(servo_bus.vin_read(2))
    # servo_bus.id_write(1, 2)
    