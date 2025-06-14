from pathlib import Path
import pandas as pd

#def read_log_file(filepath):
#    path = Path(filepath)
#    if not path.exists():
#        raise FileNotFoundError(f"Log file not found: {filepath}")
#    with open(path, 'r', encoding='utf-8', errors='ignore') as file:
#        lines = file.readlines()
#    
#    df = pd.DataFrame(lines, columns=["log_line"])
#    return df

def read_log_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return pd.DataFrame({"line": lines})