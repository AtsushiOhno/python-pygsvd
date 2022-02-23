"""
Test
"""

import pytest
import numpy as np
from src.pygsvd import pygsvd


def test_pygsvd_real():

    a = np.arange(1, 13).reshape(4, 3)
    b = np.arange(1, 16).reshape(5, 3)

    ua, ub, da, db, xt = pygsvd(a, b)
    assert np.allclose(a, ua@da@xt)
    assert np.allclose(b, ub@db@xt)

def test_pygsvd_con():

    a = np.array([[1.j, 2.j, 3.j], [4.j, 5., 6.]])
    b = np.arange(1, 16).reshape(5, 3)

    ua, ub, da, db, xt = pygsvd(a, b)
    assert np.allclose(a, ua@da@xt)
    assert np.allclose(b, ub@db@xt)

def test_pygsvd_zero():

    a = np.tile(0, (2, 3))
    b = np.arange(1, 16).reshape(5, 3)

    ua, ub, da, db, xt = pygsvd(a, b)
    assert np.allclose(a, ua@da@xt)
    assert np.allclose(b, ub@db@xt)