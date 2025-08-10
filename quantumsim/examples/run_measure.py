from quantumsim.core.circuit import Circuit
from quantumsim.core.executor import Executor

c = Circuit(2)
c.h(0).cx(0,1)

sv = Executor().run(c)
print("Counts from 1000 shots:", sv.measure_all(1000))