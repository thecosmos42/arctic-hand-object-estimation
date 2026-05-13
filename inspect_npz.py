"""Print the keys and array shapes inside a .npz file."""
import sys
import numpy as np
from pathlib import Path

def inspect(npz_path: Path) -> None:
    if not npz_path.exists():
        sys.exit(f"File not found: {npz_path}")
    data = np.load(npz_path, allow_pickle=False)
    print(f"File: {npz_path.name}")
    print(f"Number of arrays: {len(data.files)}\n")
    for key in data.files:
        arr = data[key]
        print(f"  {key:<20s}  dtype={arr.dtype!s:>7s}  shape={arr.shape}")
    data.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <file.npz>")
        sys.exit(1)
    inspect(Path(sys.argv[1]))
