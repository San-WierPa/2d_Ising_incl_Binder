# tests/test_utils.py

import unittest
import numpy as np
from src.py_ising_2d.utils import calc_magnetisation, initial_lattice

class TestLatticeFunctions(unittest.TestCase):

    def test_calc_magnetisation(self):
        spinconfig = np.array([[1, -1], [1, 1]])
        self.assertEqual(calc_magnetisation(spinconfig), 2)

    def test_initial_lattice(self):
        n = 4
        lattice = initial_lattice(n)
        self.assertEqual(lattice.shape, (4, 4))
        self.assertTrue(np.all(np.isin(lattice, [1, -1])))

if __name__ == '__main__':
    unittest.main()
