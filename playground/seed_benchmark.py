import dotenv
dotenv.load_dotenv()
import os

from profiles import Profile
from langchain.prompts import PromptTemplate

from chain import complete

template = """Question: {question}

Comment: Let's think about this step by step, but being brief to quickly answer the question.

Answer: First,  """

prompt = PromptTemplate(template=template, input_variables=["question"])

question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

LOG_DIR = os.environ.get('LOG_DIR', '')

if __name__ == '__main__':
    from tqdm.auto import trange
    import json

    all_results = []

    n_repetitions = 1
    seeds = [_ for _ in range(123, 126)]
    print(f'{len(seeds)} seeds by {n_repetitions} repetitions: {len(seeds) * n_repetitions} tests to be performed.')
    
    for seed_i in trange(len(seeds), desc='Seeds'):
        seed = seeds[seed_i]
        results = [f'SEED {seed} RESULTS:']
        for rep_j in trange(n_repetitions, desc='Repetitions'):
            result = complete({'question': question}, prompt, Profile()(max_tokens=150, seed=seed))
            # print(result)
            results.append(result)
        all_results.append(results)
    
    results_output_path = os.path.join(LOG_DIR, f'benchmark_{len(seeds)}x{n_repetitions}_70b__run5.json')

    with open(results_output_path, 'w') as f:
        json.dump(all_results, f)


### RESULTS INCONCLUSIVE - sometimes setting seed leads to deterministic output, sometimes not...