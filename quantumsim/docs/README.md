# quantumsim Documentation

## Table of Contents

1. [Getting Started](#getting-started)
2. [Basic Usage](#basic-usage)
3. [API Reference](#api-reference)
4. [Tutorials](#tutorials)
5. [Examples](#examples)
6. [Educational Resources](#educational-resources)

## Getting Started

### Installation

#### Option 1: Direct Installation (Recommended)

```bash
# Clone the repository
git clone https://github.com/Vaiditya2207/quantumsim
cd quantumsim

# Install in development mode
pip install -e .

# Or install with Jupyter support
pip install -e ".[jupyter]"
```

#### Option 2: Manual Setup

```bash
# Create virtual environment
python -m venv quantumsim-env
source quantumsim-env/bin/activate  # On Windows: quantumsim-env\Scripts\activate

# Install dependencies
pip install numpy matplotlib jupyter

# Add to Python path
export PYTHONPATH=$PWD:$PYTHONPATH
```

### Quick Start

```python
from quantumsim import Circuit, Executor, print_circuit

# Create a Bell state
circuit = Circuit(2)
circuit.h(0).cx(0, 1)

# Visualize the circuit
print_circuit(circuit)

# Execute and measure
executor = Executor()
result = executor.run(circuit)
print("Measurement counts:", result.measure_all(1000))
```

## Basic Usage

### Creating Circuits

```python
# Initialize a quantum circuit
circuit = Circuit(num_qubits=3)

# Add gates using fluent API
circuit.h(0)           # Hadamard gate
circuit.x(1)           # Pauli-X (bit flip)
circuit.cx(0, 1)       # Controlled-X (CNOT)
circuit.rz(2, np.pi/4) # Rotation around Z-axis

# Or add gates explicitly
circuit.add('H', 0)
circuit.add('CX', 0, 1)
circuit.add('RY', 2, theta=np.pi/2)
```

### Gate Library

#### Single-Qubit Gates

- `H` - Hadamard (creates superposition)
- `X` - Pauli-X (bit flip)
- `Y` - Pauli-Y (bit + phase flip)
- `Z` - Pauli-Z (phase flip)
- `S` - S gate (√Z)
- `T` - T gate (√S)
- `RX(θ)` - Rotation around X-axis
- `RY(θ)` - Rotation around Y-axis
- `RZ(θ)` - Rotation around Z-axis

#### Two-Qubit Gates

- `CX` - Controlled-X (CNOT)
- `CZ` - Controlled-Z
- `SWAP` - Swap two qubits

### Simulation and Measurement

```python
# Execute circuit
executor = Executor()
final_state = executor.run(circuit)

# Get statevector
print("Statevector:", final_state.data)

# Get measurement probabilities
probs = final_state.measure_probabilities()
print("Probabilities:", probs)

# Simulate measurements
counts = final_state.measure_all(shots=1000)
print("Measurement counts:", counts)
```

### Circuit Visualization

```python
from quantumsim import print_circuit

# ASCII visualization
print_circuit(circuit)

# Output example:
# q0: -H-●-
# q1: ---⊕-
```

### Noise Simulation

```python
from quantumsim.noise import DepolarizingChannel, AmplitudeDampingChannel

# Create noise model
noise = DepolarizingChannel(p=0.1)  # 10% depolarizing noise

# Apply noise to state
noisy_state = noise.apply_stochastic(final_state)

# Compare measurements
clean_counts = final_state.measure_all(1000)
noisy_counts = noisy_state.measure_all(1000)
print("Clean:", clean_counts)
print("Noisy:", noisy_counts)
```

## API Reference

### Core Classes

#### `Circuit(num_qubits: int)`

Represents a quantum circuit.

**Methods:**
- `add(gate_name: str, *targets: int, theta: float = None) -> Circuit`
- `h(q: int) -> Circuit` - Add Hadamard gate
- `x(q: int) -> Circuit` - Add X gate
- `cx(control: int, target: int) -> Circuit` - Add CNOT gate
- `rz(q: int, theta: float) -> Circuit` - Add RZ rotation

#### `Executor()`

Executes quantum circuits.

**Methods:**
- `run(circuit: Circuit) -> Statevector` - Execute circuit

#### `Statevector(num_qubits: int, data: np.ndarray = None)`

Represents a quantum state.

**Methods:**
- `measure_probabilities() -> np.ndarray` - Get measurement probabilities
- `measure_all(shots: int) -> Dict[str, int]` - Simulate measurements
- `copy() -> Statevector` - Create a copy

### Noise Models

#### `DepolarizingChannel(p: float)`
Depolarizing noise channel.

#### `AmplitudeDampingChannel(gamma: float)`
Amplitude damping (T1 relaxation).

#### `PhaseDampingChannel(gamma: float)`
Phase damping (T2 dephasing).

### Visualization

#### `print_circuit(circuit: Circuit, show_qubits: bool = True)`
Print ASCII representation of circuit.

## Tutorials

### Interactive Jupyter Notebooks

1. **Quantum Fundamentals** (`tutorials/01_quantum_fundamentals.ipynb`)
   - Qubits and quantum states
   - Gates and circuits
   - Superposition and entanglement
   - Measurement and probability

2. **Quantum Algorithms** (`tutorials/02_quantum_algorithms.ipynb`)
   - Deutsch's algorithm
   - Grover's search
   - Quantum Fourier Transform basics

3. **Noise and Error Correction** (`tutorials/03_noise_and_errors.ipynb`)
   - Understanding quantum noise
   - Error correction concepts
   - Fault-tolerant computing

### Starting Tutorials

```bash
# Start Jupyter notebook server
jupyter notebook quantumsim/tutorials/

# Or use the CLI
quantumsim --interactive  # Interactive circuit builder
```

## Examples

All examples are in the `examples/` directory:

```bash
# Run examples with CLI
quantumsim --example bell      # Bell state
quantumsim --example grover    # Grover's algorithm
quantumsim --example teleport  # Quantum teleportation
quantumsim --example noise     # Noise demonstration
quantumsim --example demo      # Full demonstration

# Or run directly with Python
python quantumsim/examples/run_bell.py
python quantumsim/examples/run_grover.py
```

### Example: Bell State

```python
from quantumsim import Circuit, Executor, print_circuit

# Create Bell state circuit
circuit = Circuit(2)
circuit.h(0)     # Superposition
circuit.cx(0, 1) # Entanglement

print_circuit(circuit)
# Output:
# q0: -H-●-
# q1: ---⊕-

# Execute and measure
executor = Executor()
state = executor.run(circuit)
counts = state.measure_all(1000)
print(counts)  # {'00': ~500, '11': ~500}
```

### Example: Grover's Algorithm

```python
def grovers_algorithm(marked_state=3):
    circuit = Circuit(2)
    
    # Superposition
    circuit.h(0).h(1)
    
    # Oracle (marks state |11⟩)
    circuit.cz(0, 1)
    
    # Diffusion operator
    circuit.h(0).h(1)
    circuit.x(0).x(1)
    circuit.cz(0, 1)
    circuit.x(0).x(1)
    circuit.h(0).h(1)
    
    return circuit

circuit = grovers_algorithm()
state = Executor().run(circuit)
print(state.measure_all(1000))  # Should favor |11⟩
```

## Educational Resources

### Key Quantum Computing Concepts

1. **Superposition**: Qubits can exist in multiple states simultaneously
2. **Entanglement**: Quantum correlations between particles
3. **Interference**: Quantum amplitudes can cancel or reinforce
4. **Measurement**: Extracting classical information destroys quantum superposition

### Learning Path

1. **Beginner**: Start with `tutorials/01_quantum_fundamentals.ipynb`
2. **Intermediate**: Explore algorithm examples and noise models
3. **Advanced**: Study quantum error correction and optimization

### Recommended Exercises

1. Build a 3-qubit GHZ state: `|000⟩ + |111⟩`
2. Implement quantum teleportation step-by-step
3. Create your own quantum random number generator
4. Study how noise affects different quantum states

### Further Reading

- **Books**:
  - "Quantum Computation and Quantum Information" by Nielsen & Chuang
  - "Programming Quantum Computers" by Johnston, Harrigan & Gimeno-Segovia

- **Online Resources**:
  - IBM Qiskit Textbook
  - Microsoft Quantum Development Kit
  - Quantum Computing Stack Exchange

### Performance Notes

- quantumsim handles up to ~20 qubits comfortably on a laptop
- Memory usage scales as 2^n complex numbers for n qubits
- For larger circuits, consider tensor network simulators

### Contributing

quantumsim is designed for education! Contributions welcome:
- Add new quantum algorithms
- Improve visualizations
- Create more tutorials
- Optimize performance

### License

MIT License - free for educational and research use.