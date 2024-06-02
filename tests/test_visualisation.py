import unittest
from unittest.mock import patch
import numpy as np
from src.py_ising_2d.visualisation import plot_results

class TestVisualisation(unittest.TestCase):

    @patch('src.py_ising_2d.visualisation.plt.show')
    def test_plot_results(self, mock_show):
        T = np.linspace(1.53, 3.28, 100)
        M = np.random.rand(100)
        Chi = np.random.rand(100)
        n = 2

        try:
            plot_results(T, M, Chi, n)
        except Exception as e:
            self.fail(f"plot_results raised an exception {e}")

        mock_show.assert_called_once()

if __name__ == "__main__":
    unittest.main()
