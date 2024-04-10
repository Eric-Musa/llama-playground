import json
import time
import numpy as np 

if __name__ == "__main__":
    
    test_data = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'j': 8,
        'i': 9,
    }
        
    with open('test.json', 'w') as f:
        json.dump(test_data, f)

    n_reps = 100
    import time
    import numpy as np 
    times = []
    st = time.time()
    for i in range(n_reps):
        sti = time.time()
        with open('test.json', 'r') as f:
            td = json.load(f)
        times.append(time.time() - sti)
    ft = time.time() - st
    times = np.array(times)
    print(f'total time for {n_reps} reads of a JSON file: {ft}')
    print(f'mean time: {times.mean()} seconds, variance: {times.var()} seconds^2')