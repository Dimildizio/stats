"""Trying to write own naive analogs of numpy (mostly) functions
to understand how basic statistics work"""


import numpy as np
import scipy
from matplotlib import pyplot as plt
from random import random

data = [int(random()*10) for x in range(25)]
_data = [random() for x in range(30)] + [-5,-2, 4, 2]


#np.average(data)
mean = lambda d: sum(d) / len(d)    

#np.median(data)
def median(d):
    ilist = sorted(d)
    i = len(d)/2
    ind = int(i)
    
    return (ilist[ind] + ilist[ind-1]) / 2 if i.is_integer() else ilist[ind]
    
#np.mode(data)
def mode(d):
    ilist = sorted(d)
    idict = {}
    for x in ilist:
        idict[x] = idict[x]+1 if x in idict else 1
    top = 0,0
    for x in idict:
        top = (x, idict[x]) if idict[x] > top[1] else top
    return top

#np.var(data)
def variance(data):
    d_mean = mean(data)
    ilist = [(x - d_mean)**2 for x in data]
    return (sum(ilist) / len(data))

#np.std(data)
def st_dev(data):
    return variance(data)**0.5


#amount of stds
#68.3% within 1 std, 95.5 within 2, 99.7 within 3
def outstand_std(number, data):
    difference = number - mean(data)
    return difference / st_dev(data)


#range of data
#np.amax(d) - np.amin(d)
def datarange(d):
    return max(d) - min(d)

#histogram on dataset
def my_hist(data, ranges, bins, title = 'Random data', x = "I'm X", y = "I'm Y"):
    his = np.histogram(data, range = ranges, bins = bins)
    print(his)
    plt.hist(data, range = ranges, bins = bins, edgecolor = 'black')
    plt.axvline(median(data), color = 'r', linestyle = 'solid', linewidth = 1, label = 'Median')
    plt.axvline(mean(data), color = 'y', linestyle = 'solid', linewidth = 1, label = 'Mean')
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.legend()
    plt.show()

#center of hist = mean and median
#spread = datarange(d)
#skew = symmetric, left(-tailed), right(-tailed)
#modality = uni- (one peak), bi- (two), multi- (3+), uniform distribution(no)
#outliers = piece of data far from the rest

#more troublesome for even numbers
#q2 = median(data)
#q1 = median(data[:data.index(q2)]) if index of q2 odd number 
#q3 = median(data[data.index(q2)+1:]) if index of q2 odd number

#np.quantile(data, 0.25) or 0.5, 0.75 for q1 q2 q3
#np.quantile(data, [x*0.1 for x in range(1,100)]   for decile

def get_q2(data):
    point = data[len(data) // 2]
    if len(data) % 2== 0:
        point = [len(data) // 2]
        point = (data[point] + data[point-1]) / 2
    return point

def get_q1(data, method_two = False):       #might be a bug here with 2nd method
    point = len(data) // 2
    point = data[:point-method_two]
    print(point)
    return median(point)

def get_q3(data, method_two = False):
    point = len(data) // 2
    point = data[point+1-method_two:]
    print(point)
    return median(point)

#scipy.stats.iqr(data)
def interquartile_range(data):
    return get_q3(data) - get_q1(data)


#boxplot 
distance = lambda data: interquartile_range(data) *1.5    
left_whisker = lambda data: get_q1(data) - distance(data)
right_whisker = lambda data: get_q3(data) + distance(data)

def plot_boxplot(list_of_data, labels = False):
    #here should be a check whether list_of_data is a single or nested list
    if type(labels) == list:
        plt.boxplot(list_of_data, labels = labels)
    else:
        plt.boxplot(list_of_data)
    plt.show()


