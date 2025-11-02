#!/usr/bin/env python3
"""Helper script to print photo group timestamps for naming."""

from build import group_photos_by_time

groups = group_photos_by_time()
print("Photo group timestamps (add these to src/photo_groups.yaml with custom names):\n")
print("# Example:")
print("# \"2025-06-12\": \"Mount Washington - June 2025\"")
print()

for i, group in enumerate(groups, 1):
    earliest_timestamp = min(ts for _, ts in group)
    timestamp_str = earliest_timestamp.strftime("%Y-%m-%d")
    print(f'"{timestamp_str}": "Group {i} - {len(group)} photos"')
