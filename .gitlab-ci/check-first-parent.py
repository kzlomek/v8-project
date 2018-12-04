#!/usr/bin/env python3

import os
import subprocess
import sys

if __name__ == '__main__':
    parents_cmd_result = subprocess.run(['git', 'show', '-s', '--pretty=%P', 'HEAD'], stdout=subprocess.PIPE, check=True)
    first_parent = parents_cmd_result.stdout.decode('utf-8').split(' ')[0].strip()
    current_stable_cmd_result = subprocess.run(['git', 'show', '-s', '--pretty=%H', 'origin/master'], stdout=subprocess.PIPE, check=True)
    current_stable = current_stable_cmd_result.stdout.decode('utf-8').strip()
    sys.exit(0 if current_stable == first_parent else 1)
