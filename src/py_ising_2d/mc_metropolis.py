import numpy as np
from typing import Any

def mc_metro_random(spin_config: np.ndarray, n: int, beta: float) -> np.ndarray:
    """
    Execute Monte Carlo moves using the Metropolis algorithm to satisfy the detailed balance condition.

    Parameters:
    spin_config (np.ndarray): The initial spin configuration.
    n (int): The dimension of the spin lattice.
    beta (float): The inverse temperature parameter (1/kT).

    Returns:
    np.ndarray: The updated spin configuration.
    """
    for i in range(n):
        for j in range(n):
            a = np.random.randint(0, n)
            b = np.random.randint(0, n)
            spin_lattice = spin_config[a, b]

            # Periodic Boundary Condition
            neighbours = (spin_config[(a + 1) % n, b] + spin_config[a, (b + 1) % n] +
                          spin_config[(a - 1) % n, b] + spin_config[a, (b - 1) % n])

            # Change in energy
            delta_e = 2 * spin_lattice * neighbours

            # Acceptance test
            if delta_e < 0 or np.random.random() < np.exp(-delta_e * beta):
                spin_config[a, b] = -spin_lattice

    return spin_config
