import csv
import os
import sys
from scipy import linalg
import numpy as np

""" Create a script that will wrangle and format our IO data
    and then put it into a scipy matrix, which we can then save
    and use later.

"""


[481026,	580284,	496708,	1206919,	5787100,	1458137,	1392835,	1024517,	1223897,	5133698,	3691586,	2564883,	1218544,	740624,	2706124]

def save_table(someFile, theDelimiter=',',startPoint=2,endPoint=17):
    """ loads data from csv file
    into a numpy matrix and saves
    the matrix data

    someFile csv: a csv file containing our matrix data.
    theDelimiter char: character to split columns of data, set to ','.
    
    """
    #afile = open(someFile, 'rb')
    #data = csv.reader(afile, delimiter=theDelimiter)
    data = np.genfromtxt(someFile,dtype=None,delimiter=theDelimiter,skip_header=1)
    table = [row[startPoint:endPoint] for row in data]

    A = np.matrix(table)
    A = A.astype(int)
    np.save('myMatrix',A)



if __name__ == "__main__":
    save_table(sys.argv[1])
