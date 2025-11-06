from time import sleep
from tqdm import tqdm
import sys
import time
import shutil


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    start_time = time.time()
    
    for i, elem in enumerate(lst, start=1):
        percent = i / total
        term_size = shutil.get_terminal_size().columns
        bar_length = term_size - 30
        filled_length = int(bar_length * percent)
        
        bar = "=" * filled_length + ">" + " " * (bar_length - filled_length - 1)
        elapsed = time.time() - start_time
        speed = i / elapsed if elapsed > 0 else 0

        # Build display string similar to tqdm
        sys.stdout.write(
            f"\r{int(percent * 100):3d}%|[{bar}]| {i}/{total}"
        )
        sys.stdout.flush()

        yield elem  # yield current element so user can iterate normally

    sys.stdout.write("\n")  # move to new line after completion

