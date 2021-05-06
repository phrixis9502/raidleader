import pytest
from characters import raider


@pytest.fixture
def create_raider():
    create_raider.move_speed = 1
    create_raider.x_pos = 5
    create_raider.y_pos = 5
    return raider.Raider()


def test_set_destination(create_raider):
    create_raider.set_destination(4,6)
    assert create_raider.x_dest == 4
    assert create_raider.y_dest == 6


def test_move_none(create_raider):
    # Test No Movement
    create_raider.set_destination(5,5)
    create_raider.move()
    assert create_raider.x_pos == 5
    assert create_raider.y_pos == 5

def test_move_square(create_raider):
    # Test Directly Up
    create_raider.set_destination(5,3)
    create_raider.move()
    assert create_raider.x_pos == 5
    assert create_raider.y_pos == 4

    # Test Directly Down
    create_raider.set_destination(5,7)
    create_raider.move()
    assert create_raider.x_pos == 5
    assert create_raider.y_pos == 5

    # Test Directly Left
    create_raider.set_destination(3,5)
    create_raider.move()
    assert create_raider.x_pos == 4
    assert create_raider.y_pos == 5

    # Test Directly Right
    create_raider.set_destination(7,5)
    create_raider.move()
    assert create_raider.x_pos == 5
    assert create_raider.y_pos == 5


def test_move_quadrants(create_raider):
    # Test Top Left
    assert 1==1
    # Test Top Right
    # Test Bottom Left
    # Test Bottom Right

def test_move_angles(create_raider):
    # Test off angles
    assert 1==1

def test_move_short():
    assert 1==1
