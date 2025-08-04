import pytest

@pytest.fixture
def sample_data():
    return [1,2,3,4,5]

def test_sum(sample_data):
    assert sum(sample_data) == 15

#pytest fixture is a decorator which is used to define reusable setup code that can automatically provided
# to your test functions.

#2 types of testing can be done in database- manual and automatic
