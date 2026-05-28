import yaml
from pathlib import Path

def load_yaml_f(path: Path)-> dict:
    with open(path, "r") as f:
        cfg = yaml.safe_load(f)
    return cfg