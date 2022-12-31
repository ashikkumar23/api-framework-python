import pytest

from utils.file_reader import read_file


@pytest.fixture(scope="session")
def context():
    return {}


@pytest.fixture(scope="session")
def create_data():
    yield read_file("create_booking.json")


@pytest.fixture(scope="session")
def update_data():
    yield read_file("update_booking.json")
