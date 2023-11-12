# pylint: disable=missing-docstring

import random


def play_one_game(n_toss):
    '''TO DO: return the number of heads after n_toss'''
    '''TO DO: return the number of heads after n_toss'''
    heads_counter = 0
    for i in range(n_toss):
        tail_or_heads = random.randint(0, 1)  #0=tail 1=heads
        if tail_or_heads == 0:
            heads_counter += 1
    return heads_counter


def play_n_game(n_games, n_toss):
    '''TO DO: return a dictionary.
    The keys will be the possible head counts of each game
    The values will correspond to the probability of a game ending with that number of heads.
    '''
    pass  # YOUR CODE HERE