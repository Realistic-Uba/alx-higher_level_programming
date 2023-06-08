#!/usr/bin/python3
# 100-print_tebahpla.py

"""Print the alphabet in reverse order alternating upper- and lower-case."""
p  = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - p)), end="")
    p = 32 if p == 0 else 0
