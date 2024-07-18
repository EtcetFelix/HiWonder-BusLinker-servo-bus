from hiwonderbuslinker.bus_control import ServoBus, ServoPosition
from hiwonderbuslinker.lewansoul_servo_bus import ServoBusCommunication
import logging

from typing import Dict


logger = logging.getLogger(__name__)

SERVO_ID = 1
PORT = 'COM5'
BAUDRATE = 115200
TIMEOUT = 1
BUS_IDS = [1, 2]

def pos_within_error_threshold(position_tick: int, target_position: int, error_threshold: int) -> bool:
    return position_tick - error_threshold <=  target_position <= position_tick + error_threshold


def test_get_bus_position():
    """Test that all bus positions are returned."""
    bus = ServoBus(PORT, SERVO_ID, BUS_IDS)
    with ServoBusCommunication(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT, on_enter_power_on=True) as servo_bus:
        positions = bus.get_bus_position(servo_bus)
        logger.info(f"Servo Positions: {positions}")
        assert len(positions) == len(BUS_IDS)


def test_set_bus_position():
    """Move servos and test they are moved to the correct position."""
    def _verify_positions(real_positions: Dict[int, int], target_positions: Dict[int, ServoPosition], error_threshold: int):
        """Check the result servo positions are within the error threshold of the target positions."""
        for servo_id in real_positions:
            target_position = target_positions[servo_id].position
            real_position = real_positions[servo_id]
            is_pos_within_error_threshold = pos_within_error_threshold(real_position, target_position, error_threshold)
            assert is_pos_within_error_threshold

    bus = ServoBus(PORT, SERVO_ID, BUS_IDS)
    with ServoBusCommunication(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT, on_enter_power_on=True) as servo_bus:
        error_threshold = 3
        time_s = 1
        target_positions = {
            BUS_IDS[0]: ServoPosition(BUS_IDS[0], 300), 
            BUS_IDS[1]: ServoPosition(BUS_IDS[1], 380)
        }
        bus.set_bus_position(target_positions.values(), servo_bus, time_s)

        real_positions = bus.get_bus_position(servo_bus)
        _verify_positions(real_positions, target_positions, error_threshold)

        logger.info(f"Servo Positions: {real_positions}")   
