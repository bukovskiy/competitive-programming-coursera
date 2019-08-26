#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:46:44 2019

@author: vladimiruspenskiy
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import itertools

def main():
    cards = input().split();
    sameSuit = True
    combinations = ['A,2,3,4,5','2,3,4,5,6','3,4,5,6,7','4,5,6,7,8',
                    '5,6,7,8,9', '6,7,8,9,T','7,8,9,T,J','8,9,T,J,Q',
                    '9,T,J,Q,K','T,J,Q,K,A']
 
    combinations1 = [tuple(combination.split(',')) for combination in combinations]

    suits = [card[1] for card in cards]
    
    for suit in suits:
        if(suit!=suits[0]):
            sameSuit = False
            break
    if (not sameSuit):
        print("NO")
        return False
    
    deck = [card[0] for card in cards]
#    for permutation in itertools.permutations(deck):
    
    for combination in combinations1:
        if(combination in itertools.permutations(deck)):
            print("YES")
            return True
    print("NO")
            

    

if __name__ == '__main__':
    main()