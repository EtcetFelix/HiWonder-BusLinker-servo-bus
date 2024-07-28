from hiwonderbuslinker.lewansoul_servo_bus import ServoBusCommunication
import logging

logger = logging.getLogger(__name__)

SERVO_ID = 1
PORT = 'COM5'
BAUDRATE = 115200
TIMEOUT = 1


def test_pos_read():
        """Test the pos is a valid position."""
        with ServoBusCommunication(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT, on_enter_power_on=True) as servo_bus:
            angle_tick = servo_bus.pos_read(SERVO_ID)
            assert angle_tick is not None
            assert isinstance(angle_tick, int)
            logger.info(f"tick: {angle_tick}")


def test_get_vin():
    """Test the vin command responds with a voltage higher than 0."""
    with ServoBusCommunication(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT, on_enter_power_on=True) as servo_bus:
        assert servo_bus.vin_read(SERVO_ID) > 0
        logger.info(f"Servo VIN: {servo_bus.vin_read(SERVO_ID)}")

def test_pos_set():
    """Test the servo moves to commanded position."""
    with ServoBusCommunication(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT, on_enter_power_on=True) as servo_bus:
        tick_to_set = 200
        servo_bus.pos_set(servo_id=SERVO_ID, tick=tick_to_set, time_s=.1, wait=False)
        logger.info(f"Servo pos: {servo_bus.pos_read(SERVO_ID)}")
        pos = servo_bus.pos_read(SERVO_ID)
        error_threshold = 2
        assert tick_to_set-error_threshold <=  pos <= tick_to_set+error_threshold

