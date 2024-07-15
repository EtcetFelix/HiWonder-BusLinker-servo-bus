from lewansoul_servo_bus import ServoBus
import struct

_READ_1_SIGNED_SHORT_STRUCT = struct.Struct('>h')

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


with ServoBus(port='COM5', baudrate=115200, timeout=1, on_enter_power_on=True) as servo_bus:
    # print(servo_bus.id_read(254))
    print(servo_bus.vin_read(1))
    # print(servo_bus.temp_max_limit_read(2, 'C'))
    # servo_bus.move_time_write(1, 0, 70)
    # servo_bus.mode_write(1, 'motor', -50)
    # servo_bus.mode_write(1, 'servo')
    # servo_bus.move_start(1)
    # print(servo_bus.mode_read(1))
    # print(servo_bus.id_read(2))
    # print(servo_bus.temp_read(2, units='F'))
    # servo_bus.id_write(1, 2)
    def testing_pos():
        response_bytes, angle_tick = servo_bus.pos_read(1)
        print(f"raw response: {response_bytes}, binary: {binary_format(response_bytes)}, tick: {angle_tick}")

    while True:     
        testing_pos()
        # print(servo_bus.pos_read(1))
    # while True:
    #     print(servo_bus.pos_read(1))
    # print(servo_bus.is_powered(1))


    # new_id=1
    # old_id=5
    # servo_bus.id_write(old_id, new_id)
    # response_id = servo_bus.id_read(254)
    # print(response_id)
    # print(f"id {new_id} response: {response_id}, as int: {response_id[0]}")
