import os
import time
import sys
from pathlib import Path

def check(threshold_seconds: float):
    try:
        epoch_time = time.time()
        mtime = os.path.getmtime('/tmp/healthcheck_stat')
        delta = epoch_time - mtime
    except:
        sys.exit(1)

    if delta > threshold_seconds:
        sys.exit(1)
    else:
        sys.exit(0)

def touch_stat_file():
    Path('/tmp/healthcheck_stat').touch()