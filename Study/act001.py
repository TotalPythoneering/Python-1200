#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1200: Practice for
# Beginners''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1200
# DATE: 2018-10-25 15:30:00
# FILE: act001.py
# AUTHOR: Randall Nagy
# activity: act001.py
#

def cls():
    ''' Clear the Lines on the Screen '''
    for ignore in range(100):
        print()

my_str = "Welcome to act001.py"

cls()
print("type(",type(my_str),") Value:", my_str)

print("len(",len(my_str),")")

for ch in my_str:
    print("char:", ch, "ord(", ord(ch), ")")
    
for ich in range(9818, 9828):
    print(chr(ich), end='')

    
