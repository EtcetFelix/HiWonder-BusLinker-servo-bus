from hiwonderbuslinker.lewansoul_servo_bus import ServoBusCommunication
import logging

logger = logging.getLogger(__name__)

SERVO_ID = 1
PORT = 'COM5'
BAUDRATE = 115200
TIMEOUT = 1


def test_pos_read():
        with ServoBusCommunication(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT, on_enter_power_on=True) as servo_bus:
            angle_tick = servo_bus.pos_read(1)
            assert angle_tick is not None
            logger.info(f"tick: {angle_tick}")


def test_get_vin():
    with ServoBusCommunication(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT, on_enter_power_on=True) as servo_bus:
        assert servo_bus.vin_read(SERVO_ID) > 0
        logger.info(f"Servo VIN: {servo_bus.vin_read(SERVO_ID)}")

def test_set_pos():
    with ServoBusCommunication(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT, on_enter_power_on=True) as servo_bus:
        servo_bus.pos_set(servo_id=SERVO_ID, tick=200, time_s=.1, wait=False)

