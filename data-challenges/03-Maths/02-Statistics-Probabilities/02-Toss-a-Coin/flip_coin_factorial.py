# pylint: disable=missing-docstring

import math

def count_possibilities(n_toss, n_heads):
    '''TO DO: return the number of possibilities to get n_heads when flipping the coin n_toss times
        Ex: count_possibilities(4, 4)  = 1'''
    n = n_toss
    h = n_heads
    return math.factorial(n) / (math.factorial(h) * math.factorial(n - h))


def count_total_possibilities(n_toss):
    '''TO DO: '''
    return 2**n_toss


def probability(n_toss):
    '''TO DO: return a dictionary. The keys will be the possible number of heads in each game,
            so they can't be over `n_toss` or under 0. The values for each of those keys will correspond
            to the probability of a game ending with that result.
      probability(5) = {0: ..., 1:..., 2:..., 3:..., 4:..., 5:...}'''
    dic = {}

    for r in range(n_toss + 1):
        n_c_r = count_possibilities(n_toss, r)
        dic[r] = n_c_r / count_total_possibilities(n_toss)
    return dic
