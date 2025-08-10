# Quantum Projects - Educational Quantum Computing Platform

A comprehensive quantum computing education platform featuring an advanced quantum simulator and interactive learning environment.

## Project Overview

This repository contains two complementary projects for quantum computing education:

### 1. quantumsim - Advanced Quantum Simulator
A production-ready educational quantum simulator with advanced features including:
- Core quantum circuit simulation with high-performance statevector operations
- Advanced visualization tools for quantum states and circuits
- Machine learning integration for quantum ML algorithms
- Quantum error correction implementations
- Noise modeling for realistic quantum simulations
- Performance optimization and adaptive simulation

### 2. qsij - Quantum Simulator Interactive Jupyter
An interactive Jupyter-based learning environment that provides:
- One-click quantum computing learning setup
- Progressive educational notebooks from basics to advanced topics
- Pre-configured Jupyter server with quantumsim pre-loaded
- Interactive examples and hands-on exercises
- Local development environment for quantum programming

## Quick Start

### Option 1: Interactive Learning (Recommended for Beginners)
```bash
# Clone the repository
git clone https://github.com/Vaiditya2207/quantum-projects.git
cd quantum-projects/qsij

# Start the interactive learning environment
./start_quantum_server.sh

# Your browser will open to http://localhost:3032
```

### Option 2: Install quantumsim Package
```bash
# Install from PyPI (once published)
pip install quantumsim-edu

# Or install from source
git clone https://github.com/Vaiditya2207/quantum-projects.git
cd quantum-projects
pip install -e .
```

### Option 3: Development Setup
```bash
git clone https://github.com/Vaiditya2207/quantum-projects.git
cd quantum-projects

# Install in development mode
pip install -e .[dev]

# Run tests
pytest quantumsim/
```

## 🚀 Installation and Usage Guide

### 📦 Installation Methods

#### Method 1: Install from PyPI (Recommended)
```bash
pip install quantumsim-edu
```

#### Method 2: Install from GitHub
```bash
pip install git+https://github.com/Vaiditya2207/quantum-projects.git#subdirectory=quantumsim
```

#### Method 3: Local Development Installation
```bash
git clone https://github.com/Vaiditya2207/quantum-projects.git
cd quantum-projects/quantumsim
pip install -e .
```

### 🔧 How to Import and Use

#### Basic Imports
```python
# For users who installed via pip install quantumsim-edu
from quantumsim import Circuit, Executor, print_circuit, GATES
from quantumsim.core import Statevector
from quantumsim.noise import DepolarizingChannel
```

### 💻 Example Code for Users

#### 1. Create Your First Quantum Circuit

```python
from quantumsim import Circuit, Executor, print_circuit

# Create a 2-qubit circuit
circuit = Circuit(2)

# Add gates using fluent API
circuit.h(0)        # Hadamard gate on qubit 0
circuit.cx(0, 1)    # CNOT gate: control=0, target=1

# Visualize the circuit
print("Circuit diagram:")
print_circuit(circuit)

# Execute the circuit
executor = Executor()
result = executor.run(circuit)

# Get measurement results
counts = result.measure_all(shots=1000)
print(f"Bell state measurements: {counts}")
# Expected output: {'00': ~500, '11': ~500}
```

#### 2. Grover's Search Algorithm

```python
from quantumsim import Circuit, Executor, print_circuit

def grovers_algorithm(target_state="11"):
    """Grover's algorithm to find a marked state in a 2-qubit system"""
    circuit = Circuit(2)
    
    # Step 1: Initialize superposition
    circuit.h(0).h(1)
    
    # Step 2: Oracle - mark the target state |11⟩
    if target_state == "11":
        circuit.cz(0, 1)  # Phase flip for |11⟩
    
    # Step 3: Diffusion operator (inversion about average)
    circuit.h(0).h(1)
    circuit.x(0).x(1)
    circuit.cz(0, 1)
    circuit.x(0).x(1)
    circuit.h(0).h(1)
    
    return circuit

# Run Grover's algorithm
grover_circuit = grovers_algorithm()
print_circuit(grover_circuit)

executor = Executor()
result = executor.run(grover_circuit)
counts = result.measure_all(1000)

print(f"Grover's search results: {counts}")
# Should favor the marked state |11⟩
```

#### 3. Quantum Noise Simulation

```python
from quantumsim import Circuit, Executor
from quantumsim.noise import DepolarizingChannel

def noise_demonstration():
    # Create a Bell state
    circuit = Circuit(2)
    circuit.h(0).cx(0, 1)
    
    executor = Executor()
    clean_state = executor.run(circuit)
    
    # Apply noise
    noise_channel = DepolarizingChannel(p=0.1)  # 10% noise
    noisy_state = noise_channel.apply_stochastic(clean_state)
    
    # Compare measurements
    clean_counts = clean_state.measure_all(1000)
    noisy_counts = noisy_state.measure_all(1000)
    
    print("Clean Bell state measurements:", clean_counts)
    print("Noisy Bell state measurements:", noisy_counts)

noise_demonstration()
```

#### 4. Learning Path for Students

```python
from quantumsim import Circuit, Executor

# Lesson 1: Understanding |0⟩ and |1⟩ states
def lesson_1_basic_states():
    print("=== Lesson 1: Basic Quantum States ===")
    
    # |0⟩ state (default)
    circuit = Circuit(1)
    result = Executor().run(circuit)
    print(f"|0⟩ state: {result.data}")
    
    # |1⟩ state
    circuit = Circuit(1)
    circuit.x(0)
    result = Executor().run(circuit)
    print(f"|1⟩ state: {result.data}")

# Lesson 2: Superposition
def lesson_2_superposition():
    print("\n=== Lesson 2: Superposition ===")
    
    circuit = Circuit(1)
    circuit.h(0)
    result = Executor().run(circuit)
    print(f"|+⟩ state (superposition): {result.data}")
    
    # Measure many times to see probability
    counts = result.measure_all(1000)
    print(f"Measurements: {counts}")

# Lesson 3: Entanglement
def lesson_3_entanglement():
    print("\n=== Lesson 3: Entanglement ===")
    
    circuit = Circuit(2)
    circuit.h(0)      # Create superposition
    circuit.cx(0, 1)  # Create entanglement
    
    result = Executor().run(circuit)
    print(f"Bell state: {result.data}")
    
    counts = result.measure_all(1000)
    print(f"Entangled measurements: {counts}")

# Run lessons
lesson_1_basic_states()
lesson_2_superposition()
lesson_3_entanglement()
```

### 📚 Quick Reference

#### Common Gate Operations
```python
from quantumsim import Circuit
import numpy as np

circuit = Circuit(3)

# Single-qubit gates
circuit.h(0)           # Hadamard
circuit.x(1)           # Pauli-X (NOT)
circuit.y(2)           # Pauli-Y
circuit.z(0)           # Pauli-Z
circuit.s(1)           # S gate
circuit.t(2)           # T gate

# Two-qubit gates
circuit.cx(0, 1)       # CNOT (control=0, target=1)
circuit.cz(1, 2)       # Controlled-Z
circuit.swap(0, 2)     # SWAP qubits

# Rotation gates (with angle in radians)
circuit.rx(0, np.pi/2) # Rotation around X
circuit.ry(1, np.pi/4) # Rotation around Y
circuit.rz(2, np.pi)   # Rotation around Z
```

#### Measurement and Analysis
```python
from quantumsim import Circuit, Executor

circuit = Circuit(2)
circuit.h(0).cx(0, 1)

executor = Executor()
result = executor.run(circuit)

# Get the statevector
print(f"Statevector: {result.data}")

# Get measurement probabilities
probs = result.measure_probabilities()
print(f"Probabilities: {probs}")

# Simulate measurements
counts_100 = result.measure_all(100)    # 100 shots
counts_1000 = result.measure_all(1000)  # 1000 shots
print(f"100 shots: {counts_100}")
print(f"1000 shots: {counts_1000}")

# Copy state for further operations
state_copy = result.copy()
```

## Features

### quantumsim Core Features
- **Quantum Circuit Simulation**: Support for arbitrary quantum circuits with common gates
- **Statevector Operations**: Efficient quantum state manipulation and measurement
- **Advanced Algorithms**: Implementation of Grover's search, quantum Fourier transform, VQE, QAOA
- **Error Correction**: Three-qubit codes, surface codes, and noise channel simulation
- **Machine Learning**: Quantum neural networks, kernel methods, and hybrid algorithms
- **Visualization**: ASCII circuit diagrams, Bloch sphere plots, and probability distributions
- **Performance Tools**: Circuit optimization, profiling, and adaptive simulation strategies

### qsij Learning Environment
- **Progressive Curriculum**: Structured learning path from quantum basics to advanced topics
- **Interactive Notebooks**: Hands-on Jupyter notebooks with live code examples
- **Zero Setup**: One-command startup with all dependencies pre-configured
- **Local Development**: Secure local environment for learning and experimentation
- **Educational Examples**: Curated examples covering key quantum computing concepts

## Educational Content

The platform includes comprehensive educational materials:

1. **00_welcome.ipynb** - Introduction to quantum computing and the platform
2. **01_quantum_basics.ipynb** - Fundamental quantum concepts and qubits
3. **02_building_circuits.ipynb** - Creating and manipulating quantum circuits
4. **03_quantum_algorithms.ipynb** - Implementation of major quantum algorithms
5. **04_advanced_quantum.ipynb** - Advanced topics including error correction and quantum ML

Plus example notebooks covering:
- Quantum teleportation protocol
- Bell states and entanglement
- Quantum random number generation
- Grover's search algorithm
- Quantum Fourier transform

## Target Audience

This platform is designed for:

- **Students** learning quantum computing fundamentals
- **Educators** teaching quantum concepts with hands-on examples
- **Researchers** prototyping quantum algorithms and exploring new concepts
- **Developers** building quantum applications and gaining practical experience
- **Self-learners** interested in quantum computing and quantum mechanics

## Technical Requirements

- Python 3.8 or higher
- NumPy, SciPy, Matplotlib for scientific computing
- Jupyter/JupyterLab for interactive notebooks
- Modern web browser for Jupyter interface

## Installation and Setup

### System Requirements
- macOS, Linux, or Windows
- Python 3.8+
- 4GB RAM minimum (8GB recommended for larger circuits)
- Modern web browser

### Dependencies
All dependencies are automatically installed with the package or through the setup scripts.

## Documentation and Support

- **Source Code**: [https://github.com/Vaiditya2207/quantum-projects](https://github.com/Vaiditya2207/quantum-projects)
- **Documentation**: Available in the `/docs` directories of each project
- **Examples**: Comprehensive examples in `/examples` and `/notebooks` directories  
- **Issues**: Report bugs and request features through GitHub Issues

## Contributing

We welcome contributions to improve the platform:

1. Fork the repository
2. Create a feature branch
3. Add your improvements (code, documentation, examples)
4. Submit a pull request

Areas where contributions are especially welcome:
- Additional quantum algorithms and examples
- Educational content and tutorials
- Performance optimizations
- Visualization improvements
- Hardware integration

## License

This project is licensed under the MIT License - see the individual LICENSE files for details.

## Author

**Vaiditya Tanwar**
- GitHub: [@Vaiditya2207](https://github.com/Vaiditya2207)
- Email: vaiditya2207@gmail.com

## Acknowledgments

This project builds upon fundamental quantum computing concepts and educational approaches from the quantum computing research community. Special thanks to the developers of NumPy, SciPy, Matplotlib, and Jupyter for providing the foundation for this educational platform.

## Version History

- **v2.0.0** - Complete rewrite with advanced features, ML integration, and comprehensive educational content
- **v1.x** - Initial educational quantum simulator implementation

## Future Roadmap

- Hardware integration with real quantum devices
- Advanced quantum error correction protocols
- Quantum cryptography and communication protocols
- Integration with popular quantum computing frameworks
- Cloud-based learning environment
- Mobile-friendly interface

Start your quantum computing journey today with quantumsim and qsij!
