import os, sys, pytest
import numpy as np
sys.path.append(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
))
import singen as sg
from math import pi

def test_loka_3_single_values():
    assert sg.singen(
        loka = 3,
        alternative = 3,
    ) == pytest.approx(0)
    assert sg.singen(
        loka = 3,
        alternative = 2,
    ) == pytest.approx(-0.866025)
    assert sg.singen(
        loka = 3,
        alternative = 1,
    ) == pytest.approx(0.866025)
    assert sg.singen(
        loka = 3,
        alternative = 4,
    ) == pytest.approx(0.866025)

def test_getting_zeros():
    test_list = [
        sg.singen(
            time = t,
            frequency = 0,
        ) for t in range(10)
    ]
    assert test_list == pytest.approx(
        [0,0,0,0,0,0,0,0,0,0]
    )

def test_getting_ones():
    test_list = [
        sg.singen(
            time = t,
            frequency = 0,
            phase_offset = 0.5,
        ) for t in range(10)
    ]
    assert np.shape(test_list) == (10,)
    assert test_list == pytest.approx(
        [1,1,1,1,1,1,1,1,1,1]
    )

def test_no_arguments():
    assert sg.singen() == pytest.approx(0)

def test_singen_to_zeros():
    singen_function = sg.get_2d_singen(
        func=sg.singen,
        frequency=0,
        sampling_rate=10,
        loka=2,
    )
    array = sg.two_d_function_to_numpy(
        singen_function,
        length=10,
        channels=1,
    )
    # raise BaseException(array)
    assert np.shape(array) == (10, 1)
    assert array == pytest.approx(
        [0,0,0,0,0,0,0,0,0,0]
    )

def test_singen_to_ones():
    singen_function = sg.get_2d_singen(
        func=sg.singen,
        frequency=0,
        sampling_rate=10,
        loka=2,
    )
    array = sg.two_d_function_to_numpy(
        lambda x,y: singen_function(x, y) + 1,
        length=10,
        channels=1,
    )
    # raise BaseException(array)
    assert np.shape(array) == (10, 1)
    assert array == pytest.approx(
        [1,1,1,1,1,1,1,1,1,1]
    )


def test_singen_to_numpy_loka5():
    singen_function = sg.get_2d_singen(
        func=sg.singen,
        frequency=0,
        sampling_rate=30,
        loka=5,
    )
    array = sg.two_d_function_to_numpy(
        lambda x,y: singen_function(x, y),
        length=300,
        channels=5,
    )
    assert np.shape(array) == (300, 5)
