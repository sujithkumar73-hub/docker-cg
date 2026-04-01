import numpy as np
import pandas as pd
print("Hello from Python inside Docker!")

print("Numpy version:", np.__version__)
print("Pandas version:", pd.__version__)

numbers = list(range(1, 6))
print(numbers)