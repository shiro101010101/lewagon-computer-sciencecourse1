import math
from numpy.core.fromnumeric import sort
from collections import Counter


def my_mean(samples):
    '''returns the mean of the observations'''
    return sum(samples)/len(samples)


def my_standard_deviation(samples):
    '''returns the standard deviation of the observations'''
    mean=sum(samples)/len(samples)
    num=len(samples)-1
    sigma_right=[(x - mean)**2 for x in samples]
    sigma_lef_right=sum(sigma_right)
    return math.sqrt(sigma_lef_right/num)

def my_mode(samples):
    '''returns the mode of the observations'''
    c_1=Counter(samples)
    lis=[num for num,fre in c_1.items() if fre == c_1.most_common(1)[0][1]]
    for i in lis:
        return i



def my_multimodes(samples):
    '''returns the modes of the observations as a sorted list'''
    c_1=Counter(samples)
    lis=[num for num,fre in c1.items() if fre == c1.most_common(1)[0][1]]
    return sort(lis)

def my_median(samples):
    '''returns the median of the observations'''
    n=len(samples)
    index=n//2 #the floor division // rounds the result down to the nearest whole number
    if n%2:#odd number
        return sorted(samples)[index]
    #even number
    return sum(sorted(samples)[index-1:index+1])/2
