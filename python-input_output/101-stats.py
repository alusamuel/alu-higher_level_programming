#!/usr/bin/python3
"""Reads from stdin, computes and prints metrics every 10 lines."""

import sys

def print_stats(file_size, status_counts):
    """Prints accumulated file size and status code counts in sorted order."""
    print(f"File size: {file_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

file_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 2:
            continue

        # Update file size
        try:
            file_size += int(parts[-1])
        except ValueError:
            continue

        # Update status code count if it exists in the dictionary
        try:
            status_code = int(parts[-2])
            if status_code in status_counts:
                status_counts[status_code] += 1
        except ValueError:
            continue

        # Increment line count and print stats every 10 lines
        line_count += 1
        if line_count % 10 == 0:
            print_stats(file_size, status_counts)

except KeyboardInterrupt:
    pass

finally:
    # Print final stats
    print_stats(file_size, status_counts)
