# Source code for a resonator class

import numpy as np


class Resonator(object):
    """Return a microwave frequency resonator object."""

    def __init__(self, omega: float, dim: int):
        self.omega = omega
        self.dim = dim

    def number_operator(self) -> np.ndarray:
        """Return the number operator for the resonator"""
        return np.diag(np.arange(0, self.dim, 1))

    def annihilation_operator(self) -> np.ndarray:
        """Return the annihilation operator for the resonator"""
        return np.diag(np.sqrt(np.arange(1, self.dim)), k=1)

    def creation_operator(self) -> np.ndarray:
        """Return the creation operator for the resonator"""
        return np.diag(np.sqrt(np.arange(1, self.dim, 1)), k=-1)
