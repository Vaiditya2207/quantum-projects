"""Command line interface for quantumsim."""

import argparse
import sys
from pathlib import Path
from quantumsim import Circuit, Executor, print_circuit
from quantumsim.examples import demo_all


def run_circuit_file(filepath: str):
    """Run a circuit from a Python file."""
    try:
        # Execute the file in quantumsim context
        with open(filepath, 'r') as f:
            code = f.read()
        
        # Create execution namespace with quantumsim imports
        namespace = {
            'Circuit': Circuit,
            'Executor': Executor,
            'print_circuit': print_circuit,
            '__name__': '__main__'
        }
        
        exec(code, namespace)
        
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error executing circuit: {e}")
        sys.exit(1)


def list_examples():
    """List available example circuits."""
    examples = [
        "run_bell.py - Bell state preparation and measurement",
        "run_grover.py - Grover's search algorithm (2-qubit)",
        "run_teleport.py - Quantum teleportation protocol", 
        "run_noise_demo.py - Demonstration of quantum noise effects",
        "demo_all.py - Comprehensive feature demonstration"
    ]
    
    print("Available examples:")
    for example in examples:
        print(f"  • {example}")
    print("\nRun with: quantumsim --example <name>")


def run_example(name: str):
    """Run a built-in example."""
    example_map = {
        'bell': 'run_bell.py',
        'grover': 'run_grover.py',
        'teleport': 'run_teleport.py',
        'noise': 'run_noise_demo.py',
        'demo': 'demo_all.py'
    }
    
    if name in example_map:
        # Import and run the example
        import importlib.util
        import quantumsim.examples
        
        example_file = example_map[name]
        module_name = example_file.replace('.py', '')
        
        try:
            module = importlib.import_module(f'quantumsim.examples.{module_name}')
            # Most examples have a main function or run when imported
            if hasattr(module, 'main'):
                module.main()
        except ImportError as e:
            print(f"Error importing example '{name}': {e}")
            sys.exit(1)
    else:
        print(f"Example '{name}' not found.")
        list_examples()
        sys.exit(1)


def interactive_mode():
    """Start interactive circuit builder."""
    print("quantumsim Interactive Mode")
    print("=========================")
    print("Build quantum circuits step by step!")
    print("Commands: h(q), x(q), cx(c,t), measure(), quit()")
    print()
    
    num_qubits = int(input("How many qubits? (1-10): "))
    if not 1 <= num_qubits <= 10:
        print("Please choose between 1 and 10 qubits.")
        return
    
    circuit = Circuit(num_qubits)
    executor = Executor()
    
    print(f"\nCreated {num_qubits}-qubit circuit. Start building:")
    
    while True:
        try:
            print_circuit(circuit)
            cmd = input("\nqsim> ").strip().lower()
            
            if cmd == 'quit()' or cmd == 'q':
                break
            elif cmd == 'measure()':
                sv = executor.run(circuit)
                counts = sv.measure_all(1000)
                print(f"Measurement results (1000 shots): {counts}")
            elif cmd.startswith('h(') and cmd.endswith(')'):
                q = int(cmd[2:-1])
                circuit.h(q)
                print(f"Added H gate to qubit {q}")
            elif cmd.startswith('x(') and cmd.endswith(')'):
                q = int(cmd[2:-1])
                circuit.x(q)
                print(f"Added X gate to qubit {q}")
            elif cmd.startswith('cx(') and cmd.endswith(')'):
                parts = cmd[3:-1].split(',')
                c, t = int(parts[0]), int(parts[1])
                circuit.cx(c, t)
                print(f"Added CX gate: control={c}, target={t}")
            else:
                print("Unknown command. Try: h(0), x(1), cx(0,1), measure(), quit()")
                
        except (ValueError, IndexError):
            print("Invalid command format.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="quantumsim: Educational Quantum Computer Simulator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  quantumsim --example demo      # Run comprehensive demo
  quantumsim --example grover    # Run Grover's algorithm
  quantumsim --list              # List all examples
  quantumsim --interactive       # Interactive circuit builder
  quantumsim my_circuit.py       # Run custom circuit file
"""
    )
    
    parser.add_argument('file', nargs='?', 
                       help='Python file containing quantum circuit')
    parser.add_argument('--example', '-e', 
                       help='Run built-in example')
    parser.add_argument('--list', '-l', action='store_true',
                       help='List available examples')
    parser.add_argument('--interactive', '-i', action='store_true',
                       help='Interactive mode')
    parser.add_argument('--version', '-v', action='version',
                       version='quantumsim-edu 0.1.0')
    
    args = parser.parse_args()
    
    if args.list:
        list_examples()
    elif args.example:
        run_example(args.example)
    elif args.interactive:
        interactive_mode()
    elif args.file:
        run_circuit_file(args.file)
    else:
        # Default: run demo
        print("Welcome to quantumsim! Running demonstration...")
        print("(Use --help for more options)\n")
        run_example('demo')


if __name__ == '__main__':
    main()