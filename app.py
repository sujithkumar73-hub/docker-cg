import numpy as np
import pandas as pd


def get_numbers(count=5):
    """Return list of numbers from 1 to count (inclusive)."""
    return list(range(1, count + 1))


def info():
    """Return environment strings used for logging/testing."""
    return {
        "greeting": "Hello from Python inside Docker!",
        "numpy": np.__version__,
        "pandas": pd.__version__,
    }


def main():
    print(info()["greeting"])
    print("Numpy version:", info()["numpy"])
    print("Pandas version:", info()["pandas"])
    print(get_numbers())
    return get_numbers()


if __name__ == "__main__":
    main()