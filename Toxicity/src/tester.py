import pandas as pd

import os
os.environ['XLA_USE_BF16'] = "1"

from glob import glob
for path in glob(f'data/*'):
    print(path)