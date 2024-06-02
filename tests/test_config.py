import unittest
from src.py_ising_2d.config import Config
import numpy as np

class TestConfig(unittest.TestCase):

    def test_default_initialization(self):
        config = Config(n=2)
        self.assertEqual(config.beta, 0.47)
        self.assertEqual(config.n, 2)
        self.assertEqual(config.nt, 100)
        self.assertEqual(config.eq_steps, 100)
        self.assertEqual(config.mc_steps, 10000)
        self.assertEqual(len(config.T), config.nt)
        self.assertEqual(len(config.M), config.nt)
        self.assertEqual(len(config.Chi), config.nt)
        self.assertEqual(config.norm_1, 1.0 / (config.mc_steps * config.n * config.n))
        self.assertEqual(config.norm_2, 1.0 / (config.mc_steps ** 2 * config.n * config.n))
        self.assertEqual(config.Magnetizations, [])

    def test_temperature_range(self):
        config = Config(n=2)
        self.assertTrue(np.all(config.T >= 1.53))
        self.assertTrue(np.all(config.T <= 3.28))

if __name__ == "__main__":
    unittest.main()
