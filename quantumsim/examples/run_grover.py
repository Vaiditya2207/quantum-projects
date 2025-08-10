"""Grover's algorithm demonstration for 2-qubit search."""

import numpy as np
from quantumsim.core.circuit import Circuit
from quantumsim.core.executor import Executor
from quantumsim.viz.ascii import print_circuit


def create_grover_circuit(marked_state: int = 3) -> Circuit:
    """Create Grover's algorithm circuit for 2 qubits.
    
    Args:
        marked_state: The state to search for (0-3 for 2 qubits)
    """
    c = Circuit(2)
    
    # Initialize superposition
    c.h(0).h(1)
    
    # Oracle for marked state |11 (state 3)
    if marked_state == 3:  # |11
        c.cz(0, 1)  # Flips phase of |11
    elif marked_state == 2:  # |10
        c.x(1).cz(0, 1).x(1)
    elif marked_state == 1:  # |01
        c.x(0).cz(0, 1).x(0)
    elif marked_state == 0:  # |00
        c.x(0).x(1).cz(0, 1).x(0).x(1)
    
    # Diffusion operator (amplitude amplification about average)
    c.h(0).h(1)  # H⊗H
    c.x(0).x(1)  # X⊗X
    c.cz(0, 1)   # CZ
    c.x(0).x(1)  # X⊗X
    c.h(0).h(1)  # H⊗H
    
    return c


def demonstrate_grover():
    """Demonstrate Grover's algorithm."""
    print("=== Grover's Algorithm Demo (2-qubit search) ===\n")
    
    marked_state = 3  # Searching for |11
    circuit = create_grover_circuit(marked_state)
    
    print(f"Searching for state |{format(marked_state, '02b')}:")
    print_circuit(circuit)
    print()
    
    # Execute
    executor = Executor()
    final_state = executor.run(circuit)
    
    print("Final amplitudes:")
    for i, amp in enumerate(final_state.data):
        binary = format(i, '02b')
        prob = abs(amp)**2
        print(f"|{binary}: amplitude={amp:.4f}, probability={prob:.4f}")
    
    print(f"\nMeasurement simulation (1000 shots):")
    counts = final_state.measure_all(1000)
    for state, count in sorted(counts.items()):
        percentage = count / 1000 * 100
        print(f"|{state}: {count} times ({percentage:.1f}%)")
    
    print(f"\nGrover amplified the marked state |{format(marked_state, '02b')}!")


if __name__ == "__main__":
    demonstrate_grover()