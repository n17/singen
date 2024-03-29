import os, sys, pytest
import numpy as np
sys.path.append(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
))
from singen import singen, singen_to_numpy
if os.environ.get("SINGEN_TEST_IMAGES"):
    import matplotlib.pyplot as plt


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

def test_singen_to_numpy():
    array = singen_to_numpy(
        length=1,
        frequency=0,
        sampling_rate=10,
    )
    assert array == pytest.approx(
        [0,0,0,0,0,0,0,0,0,0]
    )

def test_singen_to_numpy_loka5():
    array = singen_to_numpy(
        length=10,
        frequency=0,
        sampling_rate=30,
        loka=5
    )
    assert np.shape(array) == (300, 5)

def test_plot_three_sines():
    if os.environ.get("SINGEN_TEST_IMAGES"):
        array = singen_to_numpy(
            length=10,
            frequency=0.5,
            sampling_rate=30,
            loka=3
        )
        plt.figure()
        for n in range(array.shape[1]):
            plt.plot(
                array[:, n],
                color=np.random.rand(1,3),
                linewidth=3
            )
        plt.savefig("singen_three_test_sines.png")

def test_hann_window():
    """
    Hann windows traditionally have a minimum value of 0 and a maximum
    value of 1, but this one goes from -1 to 1.
    """
    array = singen_to_numpy(
        length=1,
        frequency=1,
        sampling_rate=20,
        loka=1,
        phase_offset=-0.5,
    )
    expected_result = [
        -1.0, -0.951056516, -0.809016994, -0.587785252, -0.309016994, 0.0,
        0.309016994, 0.587785252, 0.809016994, 0.951056516, 1.0, 0.951056516,
        0.809016994, 0.587785252, 0.309016994, 1.2246468e-16, -0.309016994,
        -0.587785252, -0.809016994, -0.951056516
    ]
    assert array == pytest.approx(expected_result)
    if os.environ.get("SINGEN_TEST_IMAGES"):
        plt.figure()
        plt.plot(
            array,
            color="blue",
            linewidth=3
        )
        plt.savefig("singen_hann_window.png")
