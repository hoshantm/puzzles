#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 18:48:12 2018

@author: Tarik Hoshan
"""

def game_sequence(game, score):
    new_score = [s-1 if i != (game-1)%3 else s for i, s in enumerate(score)]
    if all(map(lambda s: s==0, new_score)):
        return True, [game]
    elif all(map(lambda s: s>=0, new_score)):
        for result in [-1,1]:
            next_game = (game+result)%3
            status, games = game_sequence(next_game, new_score)
            if status:
                games.append(game)
                return True, games
                
    return False, None
        
def find_game_sequence(score):
    for game in range(3):
        status, games = game_sequence(game, score)
        if status:
            games.reverse()
            return games
        
    return False               
        
              
if __name__ == "__main__":
    result = find_game_sequence([8,11,15])
    print(result)