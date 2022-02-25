import time
import rdtsc

t1 = rdtsc.get_cycles()
for i in range(1000000000000000000):
    print(i)
t2 = rdtsc.get_cycles()

