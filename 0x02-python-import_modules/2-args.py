#!/usr/bin/python3
import sys
n = len(sys.argv)
print("{} argument:".format(n - 1))
for x in range(1, n):
    print("{}: {}".format(x, sys.argv[x]))
