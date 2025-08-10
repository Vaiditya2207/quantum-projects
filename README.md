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
