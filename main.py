import numpy as np
import argparse
from src.py_ising_2d import Config, mc_metro_random, initial_lattice, calc_magnetisation, plot_results

def run_simulation(n, plot):
    config = Config(n=n)

    for t_index, temp in enumerate(config.T):
        M1 = 0
        M2 = 0
        spin_config = initial_lattice(config.n)
        beta = 1.0 / temp

        # Equilibrate the system
        for _ in range(config.eq_steps):
            mc_metro_random(spin_config, config.n, beta)

        # Perform Monte Carlo steps
        for _ in range(config.mc_steps):
            mc_metro_random(spin_config, config.n, beta)
            mag = calc_magnetisation(spin_config)

            M1 += mag
            M2 += mag * mag

        # Store results
        config.M[t_index] = config.norm_1 * M1
        config.Chi[t_index] = (config.norm_1 * M2 - config.norm_2 * M1 * M1) * beta

    # Output results for the current lattice size
    print(f"Lattice size {n} completed.")
    print("\nMagnetizations:")
    print(np.array2string(config.M, formatter={'float_kind':lambda x: "%.4f" % x}))
    print("\nSusceptibilities:")
    print(np.array2string(config.Chi, formatter={'float_kind':lambda x: "%.4f" % x}))

    # Plot the results if the plot flag is set
    if plot:
        plot_results(config.T, config.M, config.Chi, n)

def main():
    parser = argparse.ArgumentParser(description="Monte Carlo Simulation using the Metropolis algorithm.")
    parser.add_argument(
        "lattice_size",
        type=int,
        help="Size of the lattice (e.g., 4, 8, 16, 32)"
    )
    parser.add_argument(
        "--plot",
        action='store_true',
        help="Plot the results after simulation"
    )

    args = parser.parse_args()
    run_simulation(args.lattice_size, args.plot)

if __name__ == "__main__":
    main()