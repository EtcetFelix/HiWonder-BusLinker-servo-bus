from lewansoul_servo_bus import ServoBus

with ServoBus(port='COM5', baudrate=115200, timeout=1, on_enter_power_on=True) as servo_bus:
    # print(servo_bus.id_read(254))
    print(servo_bus.vin_read(1))
    # print(servo_bus.temp_max_limit_read(2, 'C'))
    # servo_bus.move_time_write(1, 0, 70)
    # servo_bus.mode_write(1, 'motor', 34)
    servo_bus.mode_write(1, 'servo')
    # servo_bus.move_start(1)
    print(servo_bus.mode_read(1))
    # print(servo_bus.id_read(2))
    # print(servo_bus.temp_read(2, units='F'))
    # servo_bus.id_write(1, 2)
    print(servo_bus.pos_read(1))
    # print(servo_bus.is_powered(1))


    # new_id=1
    # old_id=5
    # servo_bus.id_write(old_id, new_id)
    # response_id = servo_bus.id_read(254)
    # print(response_id)
    # print(f"id {new_id} response: {response_id}, as int: {response_id[0]}")
