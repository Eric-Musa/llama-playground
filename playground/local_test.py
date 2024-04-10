import time
import json
from openai_dropin import main as run_openai_dropin

n_repetitions = 20
times = []

initial_time = time.time()
for i in range(n_repetitions):
    st = time.time()
    run_openai_dropin()
    ft = time.time()
    times.append(ft-st)
    print(f'repetition {i} completed in {ft-st}. Total time elapsed: {ft-initial_time}')

print(f'average time elapsed per call: {sum(times) / len(times)}')