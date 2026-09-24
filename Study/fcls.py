#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1200: Practice for
# Beginners''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1200
# DATE: 2018-10-26 15:30:00
# FILE: fcls.py
# AUTHOR: Randall Nagy
# activity: fcls.py
#

def cls():
    ''' Clear the Lines on the Screen '''
    for ignore in range(100):
        print()

def fcls():
    ''' Clear the screen, and displays full file name '''
    cls()
    zbox = '=' * 3
    print(zbox, "RESTART:", __file__, zbox)


fcls()
