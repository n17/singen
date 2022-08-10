import os, sys, pytest
sys.path.append(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
))
from singen import singen

def test_loka_3_single_values():
    assert singen(3, 0, 3, 1, 5, 10, 0) == pytest.approx(0)
    assert singen(3, 0, 2, 1, 5, 10, 0) == pytest.approx(-0.866025)
    assert singen(3, 0, 1, 1, 5, 10, 0) == pytest.approx(0.866025)


