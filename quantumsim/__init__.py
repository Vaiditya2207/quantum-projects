"""
QuantumSim Educational Package

An educational quantum computing simulator for learning and experimentation.
Provides simple APIs for building quantum circuits and running algorithms.
"""

__version__ = "2.0.3"
__author__ = "Vaiditya Tanwar"
__email__ = "vaidityatanwar2207@gmail.com"

# Core quantum simulation
from .core.circuit import Circuit
from .core.gates import Gate, GATES
from .core.statevector import Statevector
from .core.executor import Executor

# Visualization tools
from .viz.ascii import print_circuit

# Algorithms
from .algorithms.advanced import (
    grover_search,
    bernstein_vazirani, 
    quantum_phase_estimation,
    simons_algorithm
)

# Noise models
from .noise.channels import (
    bit_flip_channel,
    phase_flip_channel,
    depolarizing_channel,
    amplitude_damping_channel,
    phase_damping_channel
)

# Top-level convenience functions
def bell_state():
    """Create a Bell state circuit."""
    circuit = Circuit(2)
    circuit.h(0)
    circuit.cx(0, 1)
    return circuit

# Main exports for easy import
__all__ = [
    "Circuit", 
    "Executor", 
    "Statevector",
    "Gate",
    "GATES",
    "print_circuit",
    "bell_state",
    "grover_search",
    "bernstein_vazirani", 
    "quantum_phase_estimation",
    "simons_algorithm",
    "bit_flip_channel",
    "phase_flip_channel",
    "depolarizing_channel", 
    "amplitude_damping_channel",
    "phase_damping_channel"
]

__version__ = "2.0.0"
__author__ = "Vaiditya Tanwar"
__email__ = "vaiditya2207@gmail.com"

# Core quantum simulation components
from .core.circuit import Circuit
from .core.gates import Gate, GATES
from .core.statevector import Statevector
from .core.executor import Executor

# Visualization tools
from .viz.ascii import ASCIIDrawer, print_circuit

# Convenience functions for common circuits
def bell_state():
    """Create a Bell state circuit."""
    circuit = Circuit(2)
    circuit.h(0)
    circuit.cx(0, 1)
    return circuit

# Main exports for easy import
__all__ = [
    "Circuit", 
    "Executor", 
    "print_circuit",
    "ASCIIDrawer",
    "Gate",
    "GATES",
    "Statevector",
    "bell_state"
]