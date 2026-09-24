#!/usr/bin/env python3
# MISSION: The complete set of source code for ''Python 1200: Practice for
# Beginners''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-1200
# DATE: 2018-10-29 15:30:00
# FILE: act002_s04.py
# AUTHOR: Randall Nagy
# activity: act002_s03.py
#

def cls(msg=None, zbox = '==='):
    ''' Clear the Lines on the Screen '''
    for ignore in range(50):
        print()
    if zbox is not None:
        print(zbox, "RESTART:", __file__, zbox)
    if msg is not None:
        print(zbox, msg.upper())

cls("act002_s03.py: Function I/P/O Practice")

def calc(my_data, opers, trace=False):
    ''' Use our data to detect regressions.
    Note that 432000.0 <> the formatted 432000.0000
    
    >>> calc(list("1234554321"), ("+", "*"))
    432000.0
    >>> calc(("11.11", "22.22", "33.33", "44.44"), ("+", "*"))
    40623892.698877215
    '''
    result = 0.0
    for op in opers:
        for fval in my_data:
            expr = str(result) + op +  fval
            result = eval(expr)
            if trace:
                print(expr, "is", result)
    return result
        
# Concept: DocTest Series
if __name__ == "__main__":
    import doctest
    doctest.testmod()


    
