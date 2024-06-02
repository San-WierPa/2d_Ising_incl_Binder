# 2d_Ising_incl_Binder

[![Python package](https://github.com/San-WierPa/2d_Ising_incl_Binder/actions/workflows/python-tests.yml/badge.svg)](https://github.com/San-WierPa/2d_Ising_incl_Binder/workflows/python-tests.yml)

This package provides an implementation of the Metropolis algorithm for simulating spin configurations.

## Installation

You can install the package using pip:

```bash
pip install .
```

## Usage

Here’s an example of how to use the package to perform Monte Carlo simulations:

```python
import numpy as np
from src.py_ising_2d import Config, mc_metro_random, initial_lattice, calc_magnetisation

# Define lattice size and configuration
n = 4
config = Config(n=n)

# Initialize spin configuration
spin_config = initial_lattice(n)

# Perform Monte Carlo simulation
for t_index, temp in enumerate(config.T):
    beta = 1.0 / temp

    # Equilibrate the system
    for _ in range(config.eq_steps):
        mc_metro_random(spin_config, n, beta)

    # Perform Monte Carlo steps
    for _ in range(config.mc_steps):
        mc_metro_random(spin_config, n, beta)
        mag = calc_magnetisation(spin_config)

        config.M[t_index] += mag
        config.Chi[t_index] += mag * mag

    # Normalize results
    config.M[t_index] *= config.norm_1
    config.Chi[t_index] = (config.Chi[t_index] * config.norm_1 - (config.M[t_index] ** 2)) * beta

print(f"Magnetizations: {config.M}")
print(f"Susceptibilities: {config.Chi}")
```

## Plotting results

```python
from src.py_ising_2d.visualisation import plot_results

# Plot results
plot_results(config.T, config.M, config.Chi, n)
```

## Running tests

```bash
python -m unittest discover tests
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.