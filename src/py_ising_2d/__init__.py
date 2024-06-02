# src/my_package/__init__.py

from .utils import calc_magnetisation, initial_lattice
from .mc_metropolis import mc_metro_random
from .config import Config
from .visualisation import plot_results

__all__ = ["calc_magnetisation", "initial_lattice", "mc_metro_random", "Config", "plot_results"]