#!/usr/bin/python3
"""reducer.py"""
import json
import sys
values = []
for line in sys.stdin:
    #print(line)
    line = line.strip()
    data = line.split('\t')
    js = data[1].strip()
    js = js.replace("\'", "\"")
    js = json.loads(js)
    values.append(js)
max = 0 
largestCircle = dict()
for value in values:
    if value['circleSize'] > max:
        max = value['circleSize']
        largestCircle = value
largestCircleSet = set(largestCircle['circle'])
maxIntersection = 0
mostSimilar = dict()
for value in values:
    if value['fileName'] != largestCircle['fileName']:
        if len(largestCircleSet.intersection(set(value['circle']))) > maxIntersection:
            maxIntersection = len(largestCircleSet.intersection(set(value['circle'])))
            mostSimilar = value
#import re
#user = re.findall(r'\d+', largestCircle['filename'])
#similarUser = re.findall(r'\d+', mostSimilar['filename'])
#print((user[1], largestCircle['circleID'], largestCircle['CircleSize']), (similarUser[1], mostSimilar['circleID']))
print(("Largest Circle and it's size: ", largestCircle['fileName'], largestCircle['circleID'], largestCircle['circleSize']),("Most similar User and their circle",mostSimilar['fileName'], mostSimilar['circleID']))