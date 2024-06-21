#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
"""
import sys
import re


pattern = r'\s*(?P<ip>\S+)\s*' \
          r'\s*\[(?P<date>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\]' \
          r'\s*"(?P<request>[^"]*)"\s*' \
          r'\s*(?P<status_code>\d{3})' \
          r'\s*(?P<file_size>\d+)'


total_file_size = 0
status_codes_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}

line_count = 0

try:
    for line in sys.stdin:
        line_count += 1

        match = re.search(pattern, line.strip())

        # Check if the line matches the expected format
        if match:
            ip = match.group('ip')
            date = match.group('date')
            request = match.group('request')
            status_code = int(match.group('status_code'))
            file_size = float(match.group('file_size'))

            total_file_size += file_size

            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print(f'Total file size: File size: {total_file_size:.2f}')
            for status_code, count in sorted(status_codes_count.items()):
                if count > 0:
                    print(f'{status_code}: {count}')

    # Print final results
    print(f'Total file size: File size: {total_file_size:.2f}')
    for status_code, count in sorted(status_codes_count.items()):
        if count > 0:
            print(f'{status_code}: {count}')

except KeyboardInterrupt:
    print("\nInterrupted by FAE.")
