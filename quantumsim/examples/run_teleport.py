"""Quantum teleportation demonstration using quantumsim."""

import numpy as np
from quantumsim.core.circuit import Circuit
from quantumsim.core.executor import Executor
from quantumsim.viz.ascii import print_circuit


def create_teleportation_circuit() -> Circuit:
    """Create a quantum teleportation circuit.
    
    Teleports |ψ⟩ = α|0⟩ + β|1⟩ from qubit 0 to qubit 2.
    Qubits: 0 (message), 1 (Alice's EPR), 2 (Bob's EPR)
    """
    c = Circuit(3)
    
    # Prepare message state |ψ⟩ = (|0⟩ + i|1⟩)/√2 on qubit 0
    c.h(0).s(0)  # H|0⟩ then S to get (|0⟩ + i|1⟩)/√2
    
    # Create Bell pair between Alice (q1) and Bob (q2)
    c.h(1).cx(1, 2)
    
    # Alice's Bell measurement on qubits 0,1
    c.cx(0, 1).h(0)
    
    # (In reality, Alice measures q0,q1 and sends classical bits to Bob)
    
    # Bob's conditional operations (we'll apply all for demo)
    # If Alice got |00⟩: Bob does nothing
    # If Alice got |01⟩: Bob applies X
    # If Alice got |10⟩: Bob applies Z  
    # If Alice got |11⟩: Bob applies XZ
    
    # For demo, we'll show the circuit structure
    # Real implementation would use measurement results
    
    return c


def demonstrate_teleportation():
    """Demonstrate quantum teleportation."""
    print("=== Quantum Teleportation Demo ===\n")
    
    # Create teleportation circuit
    circuit = create_teleportation_circuit()
    
    print("Teleportation Circuit:")
    print_circuit(circuit)
    print()
    
    # Execute
    executor = Executor()
    final_state = executor.run(circuit)
    
    print("Final statevector (after teleportation protocol):")
    for i, amp in enumerate(final_state.data):
        if abs(amp) > 1e-10:
            binary = format(i, '03b')
            print(f"|{binary}⟩: {amp:.4f}")
    
    print("\nNote: In real teleportation, Bob's qubit state depends on")
    print("Alice's measurement outcomes and classical communication.")


if __name__ == "__main__":
    demonstrate_teleportation()