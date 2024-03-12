#!/usr/bin/python3
for m in range(ord('a'), ord('z') + 1):
    if chr(m) != 'e' and chr(m) != 'q':
        print('{:c}'.format(m), end='')

