#!/usr/bin/python3
for all_alpha in range(122, 96, -1):
    if all_alpha % 2 == 1:
        all_alpha = all_alpha - 32
    print("{:c}".format(all_alpha), end="")
