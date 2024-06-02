import matplotlib.pyplot as plt
import numpy as np

def plot_results(T, M, Chi, n):
    f = plt.figure(figsize=(18, 10))

    sp = f.add_subplot(2, 2, 1)
    plt.scatter(T, np.abs(M), s=50, marker='o', color='RoyalBlue')
    plt.xlabel("Temperature (T)", fontsize=20)
    plt.ylabel("Magnetization", fontsize=20)
    plt.title(f"Magnetization for Lattice Size {n}", fontsize=22)
    plt.axis('tight')

    sp = f.add_subplot(2, 2, 2)
    plt.scatter(T, Chi, s=50, marker='o', color='RoyalBlue')
    plt.xlabel("Temperature (T)", fontsize=20)
    plt.ylabel("Susceptibility", fontsize=20)
    plt.title(f"Susceptibility for Lattice Size {n}", fontsize=22)
    plt.axis('tight')

    plt.tight_layout()
    plt.show()