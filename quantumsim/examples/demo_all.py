"""Comprehensive demo showcasing quantumsim capabilities."""

from quantumsim import Circuit, Executor, print_circuit
from quantumsim.noise import DepolarizingChannel, AmplitudeDampingChannel


def main():
    print("quantumsim: Educational Quantum Computer Simulator")
    print("=" * 50)
    
    # 1. Basic circuit construction and visualization
    print("\n1. Basic Circuit Construction")
    c = Circuit(2)
    c.h(0).cx(0, 1)  # Bell state
    print("Bell state circuit:")
    print_circuit(c)
    
    # 2. Simulation
    print("\n2. Quantum Simulation")
    executor = Executor()
    sv = executor.run(c)
    print(f"Final state: {sv.data}")
    print(f"Probabilities: {sv.measure_probabilities()}")
    
    # 3. Measurement
    print("\n3. Measurement Simulation")
    counts = sv.measure_all(1000)
    print(f"1000 shots: {counts}")
    
    # 4. Noise effects
    print("\n4. Quantum Noise")
    # Apply noise to a single-qubit state for demo
    c_single = Circuit(1)
    c_single.h(0)  # |+⟩ state
    sv_single = executor.run(c_single)
    
    noise = DepolarizingChannel(0.15)
    noisy_sv = noise.apply_stochastic(sv_single)
    
    clean_counts = sv_single.measure_all(1000)
    noisy_counts = noisy_sv.measure_all(1000)
    print(f"Clean |+⟩ state: {clean_counts}")
    print(f"With 15% depolarizing noise: {noisy_counts}")
    
    # 5. Rotation gates
    print("\n5. Parametric Gates")
    c2 = Circuit(1)
    c2.rx(0, 3.14159/4)  # π/4 rotation
    print("X-rotation circuit:")
    print_circuit(c2)
    sv2 = executor.run(c2)
    print(f"After RX(π/4): {sv2.data}")
    
    # 6. Larger circuit
    print("\n6. Multi-Qubit Entanglement")
    c3 = Circuit(3)
    c3.h(0).cx(0, 1).cx(1, 2)  # GHZ state
    print("GHZ state |000⟩ + |111⟩:")
    print_circuit(c3)
    sv3 = executor.run(c3)
    counts3 = sv3.measure_all(1000)
    print(f"GHZ measurements: {counts3}")
    
    print("\nDemo complete! Try the algorithm examples:")
    print("  - python quantumsim/examples/run_grover.py")
    print("  - python quantumsim/examples/run_teleport.py")
    print("  - python quantumsim/examples/run_noise_demo.py")


if __name__ == "__main__":
    main()