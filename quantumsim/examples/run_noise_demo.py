"""Noise demonstration showing decoherence effects."""

import numpy as np
from quantumsim.core.circuit import Circuit
from quantumsim.core.executor import Executor
from quantumsim.noise.channels import DepolarizingChannel, AmplitudeDampingChannel
from quantumsim.viz.ascii import print_circuit


def demonstrate_noise_effects():
    """Show how noise affects quantum states."""
    print("=== Quantum Noise Effects Demo ===\n")
    
    # Create a simple circuit: |+⟩ state
    c = Circuit(1)
    c.h(0)  # |0⟩ → |+⟩ = (|0⟩ + |1⟩)/√2
    
    print("Circuit creating |+⟩ state:")
    print_circuit(c)
    print()
    
    executor = Executor()
    
    # Ideal case
    print("1. Ideal (no noise):")
    ideal_state = executor.run(c)
    print(f"   State: {ideal_state.data}")
    ideal_counts = ideal_state.measure_all(1000)
    print(f"   Measurements: {ideal_counts}")
    print()
    
    # Depolarizing noise
    print("2. With depolarizing noise (p=0.1):")
    depol_noise = DepolarizingChannel(0.1)
    # Apply noise after the gate (simplified demo)
    noisy_state = depol_noise.apply_stochastic(ideal_state)
    print(f"   State after noise: {noisy_state.data}")
    noisy_counts = noisy_state.measure_all(1000)
    print(f"   Measurements: {noisy_counts}")
    print()
    
    # Amplitude damping
    print("3. With amplitude damping (γ=0.2):")
    amp_noise = AmplitudeDampingChannel(0.2)
    damped_state = amp_noise.apply_stochastic(ideal_state)
    print(f"   State after damping: {damped_state.data}")
    damped_counts = damped_state.measure_all(1000)
    print(f"   Measurements: {damped_counts}")
    print()
    
    print("Notice how noise:")
    print("- Depolarizing: Makes measurements more random")
    print("- Amplitude damping: Biases toward |0⟩ (energy loss)")


if __name__ == "__main__":
    demonstrate_noise_effects()