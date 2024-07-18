from hiwonderbuslinker.bus_control import ServoBus
from hiwonderbuslinker.lewansoul_servo_bus import ServoBusCommunication
import logging

logger = logging.getLogger(__name__)

SERVO_ID = 1
PORT = 'COM5'
BAUDRATE = 115200
TIMEOUT = 1
BUS_IDS = [1, 2]


def test_get_bus_position():
    bus = ServoBus(PORT, SERVO_ID, BUS_IDS)
    with ServoBusCommunication(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT, on_enter_power_on=True) as servo_bus:
        positions = bus.get_bus_position(servo_bus)
        logger.info(f"Servo Positions: {positions}")
        assert len(positions) == len(BUS_IDS)


def test_set_bus_position():
    bus = ServoBus(PORT, SERVO_ID, BUS_IDS)
    with ServoBusCommunication(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT, on_enter_power_on=True) as servo_bus:
        target_positions = [300, 350]
        bus.set_bus_position(target_positions, servo_bus)
        positions = bus.get_bus_position(servo_bus)
        logger.info(f"Servo Positions: {positions}")
