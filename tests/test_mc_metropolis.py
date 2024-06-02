import unittest
import numpy as np
from src.py_ising_2d.mc_metropolis import mc_metro_random

class TestMetropolisAlgorithm(unittest.TestCase):

    def test_mc_metro_random(self):
        n = 5
        beta = 0.1
        spin_config = np.random.choice([-1, 1], size=(n, n))

        new_config = mc_metro_random(spin_config, n, beta)

        self.assertEqual(new_config.shape, (n, n))
        self.assertTrue(np.all(np.isin(new_config, [-1, 1])))

if __name__ == "__main__":
    unittest.main()
