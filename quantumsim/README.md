# quantumsim-edu: Educational Quantum Computing Simulator

A lightweight, educational quantum circuit simulator designed for learning quantum computing concepts. Built with clarity and modularity in mind, quantumsim provides an intuitive interface for building and simulating quantum circuits.

## How quantumsim Works

quantumsim uses **statevector simulation** to model quantum systems:

### Quantum State Representation
- Quantum states are represented as complex-valued vectors in a 2^n dimensional Hilbert space
- For n qubits, the statevector contains 2^n complex amplitudes
- Each amplitude represents the probability amplitude for a specific computational basis state

### Gate Operations
- Quantum gates are implemented as unitary matrices
- Gate application involves matrix-vector multiplication with the statevector
- Multi-qubit gates use tensor product operations to construct full-dimensional matrices

### Circuit Execution
- Circuits are built using a fluent API that chains gate operations
- The executor applies gates sequentially to evolve the quantum state
- Intermediate states can be inspected for educational purposes

## Features

**Core Simulation Engine:**
- Statevector simulator supporting up to 20 qubits on typical hardware
- Complete quantum gate library: Pauli gates (X, Y, Z), Hadamard (H), Phase gates (S, T), Rotation gates (RX, RY, RZ), Controlled gates (CX, CZ), SWAP gate
- Fluent circuit building API with method chaining
- ASCII circuit visualization for educational clarity

**Educational Tools:**
- Interactive examples demonstrating key quantum algorithms
- Bell state preparation and measurement
- Grover's search algorithm implementation
- Quantum teleportation protocol
- Noise modeling for realistic quantum simulation

## Installation

```bash
pip install quantumsim-edu
```

## Quick Start

```python
from core.circuit import Circuit
from core.executor import Executor

# Create a Bell state circuit
circuit = Circuit(2)
circuit.h(0)        # Apply Hadamard to qubit 0
circuit.cx(0, 1)    # Apply CNOT with control=0, target=1

# Execute the circuit
executor = Executor()
final_state = executor.run(circuit)

# Measure the result
measurement_counts = final_state.measure_all(shots=1000)
print("Measurement results:", measurement_counts)
# Expected: {'00': ~500, '11': ~500} (Bell state superposition)
```

## License

MIT License - Free for educational and research use.