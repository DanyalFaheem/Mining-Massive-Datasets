#!/usr/bin/python3
"""mapper.py"""
import sys  
import os
for line in sys.stdin:
    fileName = os.environ["map_input_file"]
    #fileName = "107"
    circle = line.split()
    from copy import deepcopy
    circleID = deepcopy(circle[0])
    del circle[0]
    circleSize = len(circle)
    dic = {"fileName": fileName, "circleID": circleID, "circleSize": circleSize, "circle": circle}
    print ("16\t", (dic))