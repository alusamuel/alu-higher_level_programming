#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - (32 * (c % 2)))), end="")
