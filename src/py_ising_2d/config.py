import numpy as np

class Config:
    def __init__(self, n: int = 4):
        self.beta = 0.47
        self.n = n
        self.nt = 100
        self.eq_steps = 100
        self.mc_steps = 10000
        self.T = np.linspace(1.53, 3.28, self.nt)
        self.M = np.zeros(self.nt)
        self.Chi = np.zeros(self.nt)
        self.norm_1 = 1.0 / (self.mc_steps * self.n * self.n)
        self.norm_2 = 1.0 / (self.mc_steps ** 2 * self.n * self.n)
        self.Magnetizations = []

# Example of how to use the config
# config = Config(n=4)
# print(config.T)
