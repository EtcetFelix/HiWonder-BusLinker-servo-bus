from hiwonderbuslinker.lewansoul_servo_bus import ServoBusCommunication
import time


SERVO_ID = 2
PORT = 'COM5'
BAUDRATE = 115200
TIMEOUT = 1


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
        angle_tick = servo_bus.pos_read(SERVO_ID)
        print(f"tick: {angle_tick}")


def get_pos_for_seconds(servo_bus, num_seconds: int):
    t_end = time.time() + num_seconds
    while time.time() < t_end:     
        testing_pos(servo_bus)
        time.sleep(num_seconds/5)

def test_move_servo_motor_for_seconds(servo_bus: ServoBusCommunication, num_seconds: int):
    servo_bus.mode_write(SERVO_ID, 'motor', 20)
    get_pos_for_seconds(servo_bus, num_seconds)
    servo_bus.mode_write(SERVO_ID, 'servo')

def test_complete_movement():
    with ServoBusCommunication(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT, on_enter_power_on=True) as servo_bus:
        # print(servo_bus.id_read(254))
        print(servo_bus.vin_read(SERVO_ID))
        print(servo_bus.pos_read(SERVO_ID))
        print(servo_bus.mode_read(SERVO_ID))
        # while True:
        #     print(servo_bus.pos_read(1))

        test_move_servo_motor_for_seconds(servo_bus, .2)
        time.sleep(0.1)
        print("sending servo move commands...")
        for x in range(1):
            servo_bus.pos_set(servo_id=1, tick=150, time_s=.1, wait=False)
            print(f"command number {x+1} sent")


if __name__ == '__main__':
    with ServoBusCommunication(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT, on_enter_power_on=True) as servo_bus:
        testing_pos(servo_bus)
        servo_bus.id_write(1, 2)
