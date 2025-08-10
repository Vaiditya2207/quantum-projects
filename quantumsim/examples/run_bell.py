from quantumsim.core.circuit import Circuit
from quantumsim.core.executor import Executor

# Build Bell state circuit
c = Circuit(2)
c.h(0).cx(0,1)

sv = Executor().run(c)
print("Final state vector:", sv.data)
print("Probabilities:", sv.measure_probabilities())