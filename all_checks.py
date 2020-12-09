#!/usr/bin/env python3

import os
import shutil
import sys

def check_reboot():
    return os.path.exist("/run/reboot-required")

def check_disk_full(disk,min_absolute,min_percent):
    '''Returns True if there isn't enough disk space, False if otherwise'''
    du = shutil.disk_usage(disk)
    #Calculate percentage of free space
    percent_free = 100 * du.free / du.total
    #Calculate how many free gigabytes
def main():
    if check_reboot():
        print('Pending Reboot')
        sys.exit(1)
    print('Everything is ok')
    sys.exit(0)

main()
