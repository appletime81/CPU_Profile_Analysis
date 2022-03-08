import os
from pprint import pprint

log_files = []
for root, dirs, files in os.walk('cpu_profile/2plus1_cores'):
    for file in files:
        log_files.append(os.path.join(root, file))

pprint(log_files)
