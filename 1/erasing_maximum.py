#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    result = []
    maximum = a[0]
    counter = 0
    index = 0
    for i in range(len(a)-1):
        if a[i+1]>=maximum:
            maximum = a[i+1];
            index = i+1
#    print(index)
#    print(maximum)
    for j in range(len(a)):
        if (a[j]== maximum):
            counter+=1
        if (counter==3):
            index=j;
            break;
#    print(index)
    a.pop(index)
    result = a
    print(" ".join(map(str,result)))


if __name__ == '__main__':
    main()