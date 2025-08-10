# Quantum Simulator Interactive Jupyter (qsij)

**Interactive Jupyter learning environment for quantum computing**

## One-Click Quantum Learning

Welcome to **qsij** - your gateway to hands-on quantum computing education! This project provides a complete Jupyter notebook environment pre-loaded with the `quantumsim` quantum simulator.

### Features

- **Local Jupyter Server** on `localhost:3032`
- **Progressive Learning Path** from basics to advanced algorithms
- **Interactive Examples** with live quantum circuit visualization
- **Pre-configured Environment** with all dependencies
- **Built-in Visualization** tools for quantum states and circuits

## Perfect For

- **Students** learning quantum computing
- **Educators** teaching quantum concepts
- **Researchers** prototyping quantum algorithms
- **Developers** exploring quantum programming
- **Anyone curious** about quantum mechanics!
- **Instant Import** - `from quantumsim import Circuit, Executor` works immediately

## Quick Start (30 seconds to quantum!)

```bash
# 1. Clone the project
git clone https://github.com/Vaiditya2207/quantum-projects
cd quantum-projects/qsij

# 2. Start the quantum learning environment
./start_quantum_server.sh

# 3. Open your browser
# Go to: http://localhost:3032
# Start coding quantum algorithms immediately!
```

## What You Get

### Pre-loaded Quantum Environment
- quantumsim v2.0 fully installed and ready
- All quantum gates and circuits available
- Visualization tools working out of the box
- No dependency management needed

### Educational Content
- **Beginner Tutorials** - Quantum basics and first circuits
- **Algorithm Examples** - Bell states, Grover's, Shor's algorithm
- **Advanced Topics** - Quantum ML, error correction, optimization
- **Interactive Exercises** - Hands-on learning with immediate feedback

### Development Tools
- **Jupyter Lab** - Modern notebook interface
- **Real-time Visualization** - See quantum states evolve
- **Easy Sharing** - Export and share your quantum experiments
- **Version Control** - Git-friendly notebook format

## Learning Path

1. **Start Here** - `01_quantum_basics.ipynb`
2. **Build Circuits** - `02_building_circuits.ipynb`
3. **Explore Algorithms** - `03_quantum_algorithms.ipynb`
4. **Advanced Topics** - `04_advanced_quantum.ipynb`

## Advanced Usage

### Custom Port
```bash
# Run on different port
JUPYTER_PORT=8888 ./start_quantum_server.sh
```

### Development Mode
```bash
# Run with auto-reload for development
./start_quantum_server.sh --dev
```

### Share Mode
```bash
# Allow external connections (use with caution)
./start_quantum_server.sh --share
```

## Project Structure

```
qsij/
├── README.md                    # This file
├── start_quantum_server.sh      # One-click server startup
├── requirements.txt             # Dependencies
├── environment.yml              # Conda environment
└── notebooks/                   # Pre-loaded quantum tutorials
    ├── 00_welcome.ipynb
    ├── 01_quantum_basics.ipynb
    ├── 02_building_circuits.ipynb
    ├── 03_quantum_algorithms.ipynb
    ├── 04_advanced_quantum.ipynb
    └── examples/
        ├── quick_examples.ipynb
        └── teleportation.ipynb
```

## Use Cases

### For Educators
```python
# In any notebook cell:
from quantumsim import Circuit, Executor

# Create quantum circuit for class demonstration
circuit = Circuit(2)
circuit.h(0).cx(0, 1)  # Bell state

# Execute and show results
executor = Executor()
state = executor.run(circuit)
print("Bell state created!")
print(state.measure_all(shots=1000))
```

### For Students
- **No Installation Required** - Works immediately after clone
- **Visual Learning** - See quantum circuits and results instantly
- **Progressive Difficulty** - Start simple, build to advanced algorithms
- **Experiment Freely** - Safe environment to try quantum concepts

### For Researchers
- **Rapid Prototyping** - Test quantum algorithms quickly
- **Easy Collaboration** - Share notebooks with colleagues
- **Documentation** - Built-in markdown for research notes
- **Reproducible Science** - Version-controlled quantum experiments

## Technical Details

### Server Configuration
- **Port**: 3032 (default, configurable)
- **Interface**: Jupyter Lab with quantum extensions
- **Security**: Local-only by default
- **Performance**: Optimized for educational workloads

### Dependencies
- quantumsim v2.0 (quantum simulator)
- JupyterLab (notebook interface)
- NumPy, Matplotlib (visualization)
- IPython widgets (interactive elements)

## Contributing

Help make quantum computing education more accessible!

```bash
# Clone and set up development environment
git clone https://github.com/Vaiditya2207/quantum-projects
cd quantum-projects/qsij
./setup_dev.sh

# Create new educational content
# Add to notebooks/ directory
# Submit pull request
```

## Support

- **Issues**: [GitHub Issues](https://github.com/Vaiditya2207/quantum-projects/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Vaiditya2207/quantum-projects/discussions)
- **Email**: vaiditya2207@gmail.com

---

## Why qsij?

> "From zero to quantum computing in 30 seconds"

qsij removes all barriers to quantum computing education:
- No complex installations
- No dependency conflicts
- No configuration required
- Clone, run, learn!

**Perfect for hackathons, workshops, classrooms, and self-study!**

Start your quantum journey today with qsij!