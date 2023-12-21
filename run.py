import time

from tqdm import tqdm

for i in tqdm(range(100), desc="Progress",unit='poach'):
    time.sleep(0.1)