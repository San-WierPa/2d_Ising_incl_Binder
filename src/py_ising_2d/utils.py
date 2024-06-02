# src/my_package/utils.py

import numpy as np
from numpy.typing import NDArray

def calc_magnetisation(spinconfig: NDArray[np.int_]) -> int:
    """
    Calculate the magnetisation of a given spin configuration.

    Parameters:
    spinconfig (NDArray[np.int_]): A 2D array representing the spin configuration of the lattice.

    Returns:
    int: The total magnetisation of the lattice.
    """
    magnetisation = np.sum(spinconfig)
    return magnetisation

def initial_lattice(n: int) -> NDArray[np.int_]:
    """
    Create an n x n lattice with a random spin configuration.

    Parameters:
    n (int): The size of the lattice (number of rows and columns).

    Returns:
    NDArray[np.int_]: A 2D array representing the initial spin configuration of the lattice.
    """
    spin_lattice = np.random.choice([1, -1], size=(n, n))
    return spin_lattice
