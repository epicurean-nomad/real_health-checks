#!/usr/bin/env python3

import os
import shutil
import sys

def check_reboot():
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk,min_gb,min_percent):
    '''Returns True if there isn't enough disk space, False if otherwise'''
    du = shutil.disk_usage(disk)
    #Calculate percentage of free space
    percent_free = 100 * du.free / du.total
    #Calculate how many free gigabytes
    gb_free = du.free / 2**30
    if percent_free < min_percent or gb_free < min_gb:
        return True
    return False
def check_root_full():
    '''Returns True if root partition is full, False otherwise'''
    return  check_disk_full(disk='/',min_gb=2,min_percent=10)
def main():
    if check_reboot():
        print('Pending Reboot')
        sys.exit(1)
    if check_root_full():
        print('Root partition full')
        sys.exit(1)

    print('Everything is ok')
    sys.exit(0)

main()
