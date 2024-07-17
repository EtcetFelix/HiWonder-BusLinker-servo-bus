from src.python.lewansoul_servo_bus import ServoBusCommunication
import struct
import time

def binary_format(data):
    binary_representation = " ".join(bin(byte)[2:].zfill(8) for byte in data)
    return binary_representation
    
def reversed_binary(data):
    # reversed_binary_representation = " ".join(bin(byte)[2:].zfill(8)[::-1] for byte in data)
    reversed_binary_representation = binary_format(data)[::-1]
    return reversed_binary_representation
    
def binary_string_to_bytes(binary_str):
    binary_str = binary_str.replace(" ", "")
    # Ensure the string has a multiple of 8 bits
    if len(binary_str) % 8 != 0:
        raise ValueError("Binary string length must be a multiple of 8")
    # Convert to integer (base 2), then to bytes
    byte_value = int(binary_str, 2)
    num_bytes = len(binary_str) // 8
    return byte_value.to_bytes(num_bytes, byteorder='big')

def reversed_byte(data):
    reversed_data = reversed_binary(data)
    bytes_obj = binary_string_to_bytes(reversed_data)
    return bytes_obj

def testing_pos(servo_bus: ServoBusCommunication):
        angle_tick = servo_bus.pos_read(1)
        print(f"tick: {angle_tick}")

def get_pos_for_seconds(servo_bus, num_seconds: int):
    t_end = time.time() + num_seconds
    while time.time() < t_end:     
        testing_pos(servo_bus)
        time.sleep(num_seconds/5)

def test_move_servo_motor_for_seconds(servo_bus: ServoBusCommunication, num_seconds: int):
    servo_bus.mode_write(1, 'motor', 20)
    get_pos_for_seconds(servo_bus, num_seconds)
    servo_bus.mode_write(1, 'servo')


with ServoBusCommunication(port='COM5', baudrate=115200, timeout=1, on_enter_power_on=True) as servo_bus:
    # print(servo_bus.id_read(254))
    print(servo_bus.vin_read(1))
    print(servo_bus.pos_read(1))
    print(servo_bus.mode_read(1))
    # while True:
    #     print(servo_bus.pos_read(1))

    test_move_servo_motor_for_seconds(servo_bus, .2)
    time.sleep(0.1)
    print("sending servo move commands...")
    for x in range(1):
        servo_bus.move_time_write(servo_id=1, tick=150, time_s=.1, wait=False)
        print(f"command number {x+1} sent")
    
    
    

