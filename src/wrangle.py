import csv
import os
import sys
from scipy import linalg
import numpy as np
import math

""" Create a script that will wrangle and format our IO data
    and then put it into a scipy matrix, which we can then save
    and use later.

"""


def save_table(someFile, theDelimiter=',',startPoint=2,endPoint=17):
    """ loads data from csv file
    into a numpy matrix and saves
    the matrix data

    someFile csv: a csv file containing our matrix data.
    theDelimiter char: character to split columns of data, set to ','.
    
    """
    # divide 1.0 by the elements so that when I use this vector in the dot product, I can use dot product and not have to iterate
    # through each element in the matrix.
    q = [1.0/389891,1.0/698562,1.0/240200,1.0/241677,1.0/3711464,1.0/648278,1.0/128054,1.0/644228,1.0/543301,1.0/2218888,1.0/2684780,1.0/72190,1.0/281067,1.0/211354,1.0/86188]
    x = [1.0/481026,1.0/580284, 1.0/496708, 1.0/1206919, 1.0/5787100, 1.0/1458137, 1.0/1392835, 1.0/1024517, 1.0/1223897, 1.0/5133698, 1.0/3691586,1.0/2564883,1.0/1218544,1.0/740624,1.0/2706124]
    #vec = np.matrix([[item] for item in r])
    afile = open(someFile, 'rb')
    data = csv.reader(afile, delimiter=theDelimiter)
    with open('betterData.csv','wb') as csvfile:
        target = csv.writer(csvfile, delimiter=',')
        for row in data:
            print row[2:17]
            target.writerow(row[2:17])

    #target.close()
    #data.close()
    data = np.genfromtxt('betterData.csv',dtype=None,delimiter=theDelimiter,skip_header=1)
    #for row in data:
    #    print row[2:]
    table = [row for row in data]
    print "printing table..\n"
    #print table
    #print('\n\ntable before loop...')
    #print table
    table2 = []
    for row in table:
        i = 0
        row2 = []
        for item in row:
            item = item*x[i]
            row2.append(math.fabs(float(item)))
            i += 1
            #print row2
        print row2
        table2.append(row2)
    print "\n\ntable2 after loop"
    print table2
    
    A = np.matrix(table2)
    A = A.astype(float)
    np.save('myMatrix',A)
    print A
    print "printing vec now.."
    vecx = np.matrix([[1.0/float(item)] for item in x])
    print vecx
    B = A.dot(vecx)
    #B = np.load('myMatrix.npy')
    print("\nB:")
    print B
    print("\n our vector d")
    vecd = vecx - B
    print vecx - B

    print ("\nNow we will compute our function to find vecx\n\
        it was vecx but yolo")
    print("computing x=(I-C)^-1 . d")

    print "..."
    # create identity matrix by computing A . inverse(A)
    I = A.dot(A.I)

    prod = (I - A)
    result = prod.I
    print result.dot(vecd)
    print "The above should be equal to vecx"
    print vecx
    



if __name__ == "__main__":
    save_table(sys.argv[1])
