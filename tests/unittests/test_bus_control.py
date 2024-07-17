import pytest

from hiwonderbuslinker.bus_control import ServoBus, ServoPosition

@pytest.fixture
def bus():
    return ServoBus('COM5', 1, [1, 2, 3])

def test_class_instantiation(bus):
    assert bus.leader_id == 1
    assert bus.servo_ids == [1, 2, 3]
    assert bus.port == 'COM5'

def test_servo_position_instantiation():
    position = ServoPosition(servo_id=1, position=10)
    assert position.servo_id == 1
    assert position.position == 10
