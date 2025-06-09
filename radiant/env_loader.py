
import os

def load_env(file_path):
    with open(file_path) as f:
        for line in f:
            if not line.strip() or line.startswith("#"):
                continue
            key, value = line.strip().split("=", 1)
            os.environ[key] = value
