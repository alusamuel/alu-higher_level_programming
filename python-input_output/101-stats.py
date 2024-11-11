#!/usr/bin/python3
"""Reads stdin line by line, computes and prints metrics every 10 lines or on interrupt."""

import sys

def print_stats(total_size, status_counts):
    """Prints file size and counts of status codes in ascending order."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 2:
            continue

        # Update total file size
        try:
            total_size += int(parts[-1])
        except ValueError:
            continue

        # Update status code count if valid
        try:
            status_code = int(parts[-2])
            if status_code in status_counts:
                status_counts[status_code] += 1
        except ValueError:
            continue

        # Print stats every 10 lines
        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    pass

finally:
    # Print final stats on exit (including if there were fewer than 10 lines)
    if line_count > 0:
        print_stats(total_size, status_counts)
