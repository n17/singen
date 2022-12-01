import os, sys, pytest
sys.path.append(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
))
from singen import singen
from math import pi

def test_loka_3_single_values():
    assert singen(
        loka = 3,
        alternative = 3,
    ) == pytest.approx(0)
    assert singen(
        loka = 3,
        alternative = 2,
    ) == pytest.approx(-0.866025)
    assert singen(
        loka = 3,
        alternative = 1,
    ) == pytest.approx(0.866025)
    assert singen(
        loka = 3,
        alternative = 4,
    ) == pytest.approx(0.866025)

def test_getting_zeros():
    test_list = [
        singen(
            time = t,
            frequency = 0,
        ) for t in range(10)
    ]
    assert test_list == pytest.approx(
        [0,0,0,0,0,0,0,0,0,0]
    )

def test_getting_ones():
    test_list = [
        singen(
            time = t,
            frequency = 0,
            phase_offset = 0.5,
        ) for t in range(10)
    ]
    assert test_list == pytest.approx(
        [1,1,1,1,1,1,1,1,1,1]
    )

def test_no_arguments():
    assert singen() == pytest.approx(0)
