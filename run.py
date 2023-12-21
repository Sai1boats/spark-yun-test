# import time
#
# from tqdm import tqdm
#
# for i in tqdm(range(100), desc="Progress",unit='poach'):
#     time.sleep(0.1)
import yaml

# import os
# print(os.getcwd())

with open('./test_data.yaml', 'r') as file:
    data = yaml.safe_load(file)
    print(data['url'])