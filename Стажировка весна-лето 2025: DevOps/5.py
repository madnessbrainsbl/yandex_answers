import os
import glob
import re
import sys

def calculate_raid_capacity(disk_sizes):
    disk_count = len(disk_sizes)
    if disk_count < 2:
        return 0

    sorted_sizes = sorted(disk_sizes, reverse=True)
    
    effective_count = disk_count if disk_count % 2 == 0 else disk_count - 1
    
    if effective_count < 2:
        return 0
    
    min_size = min(sorted_sizes[:effective_count])
    
    return min_size * (effective_count // 2)

def extract_int_after_disk(parts, line):
    for i, p in enumerate(parts):
        token = p.strip().strip('"\'').casefold()
        if 'disk' in token:
            if i + 1 < len(parts):
                next_part = parts[i+1]
                m = re.search(r'(-?\d+)', next_part)
                if m:
                    try:
                        val = int(m.group(1))
                        return val
                    except ValueError:
                        return None
            return None
    
    return None

def process_server_file(filename):
    try:
        file_size = os.path.getsize(filename)
    except OSError:
        return 0

    if file_size <= 100 or file_size > 1024:
        return 0

    disk_sizes = []
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            for raw_line in f:
                line = raw_line.strip()
                if not line:
                    continue
                parts = [p.strip() for p in line.split(',')]
                val = extract_int_after_disk(parts, line)
                if val is not None and val > 0:
                    disk_sizes.append(val)
    except Exception:
        return 0

    if not disk_sizes:
        return 0

    return calculate_raid_capacity(disk_sizes)

def main():
    prefix = sys.stdin.readline().strip()
    pattern = f"{prefix}*.csv"
    files = glob.glob(pattern)

    total_capacity = 0
    for filename in files:
        total_capacity += process_server_file(filename)

    print(total_capacity)

if __name__ == "__main__":
    main()
