#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 11:11:57 2018

@author: deola
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##################################################################################################

arr1=[3,2,1,200,4,7,8,9]


def Bubblesort(arr):
    ''' Algorithm for bubble sort'''
    for i in range(0,len(arr)):
        for j in range((len(arr)-1),i,-1):
            print i,j
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1], arr[j]
    return arr
################################################################################################
arr1=[3,2,1,200,4,7,8,9,22,11,5,21,82,34]

        #while i <len(arrLeft) and j< len(arrRight):
def LinearSearch(arr, obj):
    '''Searching for a definite object in an array'''
    for element in arr:
        #print element
        if element==obj:
            print("\n")
            print True
            
        
################################################################################################

def Mergesort(arr):
    '''Algorithm for merge sort'''
    #i,j,k=0,0,0
    
    if len(arr)<=1:
        return "Done"
    
    else:
        mid=len(arr)/2
        arrLeft=arr[mid:]
        arrRight=arr[:mid]
        print arrRight, arrLeft
        Mergesort(arrLeft)
        Mergesort(arrRight)

##############################################################################################
def MergeSearch(arr, obj):
    if len(arr)<=0:
        return "Done"
    
    else:
        mid=len(arr)/2
        arrLeft=arr[mid:]
        arrRight=arr[:mid]
        print arrRight, arrLeft
        
        #Recurively dividing        
        Mergesort(arrLeft)
        Mergesort(arrRight)       
        #Searching the divided array
        LinearSearch(arrLeft, obj)
        LinearSearch(arrRight, obj)
        
        
###############################################################################################


def Quicksort(arr):
    less = []
    equal = []
    greater = []

    if len(arr) > 1:
        pivot = arr[0]
        for x in arr:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return Quicksort(less)+equal+Quicksort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return arr

#################################################################################################################
counter=0 
ourDict=dict()     
def Recur(num, rep):
   
    global counter
    
    if rep<=1:
        return
    else:
        first=num/2
        ourDict[str(counter)]=first
        counter=counter+1     
        print "round: "+str(counter)
        if (rep-1)>1:
             ourDict.pop(str(counter-1))
        Recur( first, rep-1)
        #ourDict.pop(str(counter-1))
    return ourDict
###############################################################################################################
def NN():
    X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1],[1,0,0],[0,1,0],[0,0,0] ])
    y = np.array([[0,1,1,0,0,1,0]]).T
    syn0 = 2*np.random.random((3,3)) - 1
    syn1 = 2*np.random.random((3,1)) - 1
    
    np.random.seed(1)
    result=list()
    
    for j in xrange(60000):

        
        l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
        l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
        
        if (j% 1000) == 0:
            print "Error:" + str(np.mean(np.abs(y.T-l2)))
            result.append(np.mean(np.abs(y.T-l2)))
        Err=(y - l2)
        l2_delta = (Err)*(l2*(1-l2))
        l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1))
        syn1 += l1.T.dot(l2_delta)
        syn0 += X.T.dot(l1_delta)
        
    print("\n")
    print l2
    print("\n")
    print l1_delta 
    
    plt.title("Loss Error")
    plt.plot([a for a in range(0, len(result))], result)
    plt.show()
###########################################################################################################
###############################################################################################################        
        
def NNN():
    X= np.array([[0,1,0,1],[1,1,0,0],[1,1,1,1],[0,0,0,0],[0,0,1,1],[0,1,1,1]])
    y=np.array([[1,0,0,0,0,0]])
    
#    dataframe = pd.read_csv("/home/deola/Downloads/new_fuzzy/Dataset/mydata1_CKD.csv")
#    array = dataframe.values
#    x,y=array.shape
#    print y
#    X = array[:,0:24]
#    y = array[:,24]
    
    np.random.seed(1)
    Syn=2*np.random.random((4,9)) - 1
    Syn2=2*np.random.random((9,6)) - 1
    Syn3=2*np.random.random((6,1)) - 1
    
    result=list()
    
    for m in xrange(60000):
        
        l0=X
        l1=1/(1+np.exp(-(np.dot(l0,Syn))))
        l2=1/(1+np.exp(-(np.dot(l1,Syn2))))
        l3=1/(1+np.exp(-(np.dot(l2,Syn3))))
        
        if (m% 1000) == 0:
            print "Error:" + str(np.mean(np.abs(y.T-l3)))
            result.append(np.mean(np.abs(y.T-l3)))
            
        Err3=(y - l3)
        l_delta3=Err3*(l3*(1 - l3))
        #print Syn3.T
        Err2=l_delta3*(Syn3.T)
        l_delta2=(Err2)*(l2*(1-l2))
        
        Err1=l_delta2.dot(Syn2.T)
        l_delta1=(Err1)*(l1*(1-l1))
        
        Syn3=Syn3+np.dot(l2.T,l_delta3)
        Syn2+= np.dot(l1.T,l_delta2)
        Syn+= l0.T.dot(l_delta1)
        #print Syn
        
        
    #print l
    plt.title("Loss Error")
    plt.plot([a for a in range(0, len(result))], result)
    plt.show()
##################################################################################################
#def myfunc(func):
#    def wrapper(a,b):
#        if b==0:
#            print("cannot divide by zero")
#            return
#        else:
#            return func(a,b)
#    return wrapper
#
#@myfunc
#def original(a,b):
#    return(a/b)
#    
#print(original(2,0))
##############################################################################################

def Quadratic():
    import math
    
    a=int(input("Enter coeffient of a\n"))
    b=int(input("Enter coeffient of b\n"))
    c=int(input("Enter coeffient of c\n"))
    D=0
    
    if b*b > 4*a*c:
        D= math.sqrt(abs(b*b -4*a*c)/2*a)
        return ("x="-b/(2*a+0.0)- D), ("x="+str(-b/(2*a+0.0)+ D))
        
    elif b*b == 4*a*c:
        return ("x="+str(-b/(2*a+0.0))), ("x="+str(-b/(2*a+0.0)))
        
    elif b*b < 4*a*c:
        D="J"+str(math.sqrt(abs(b*b -4*a*c))/2*a)
        return ("x="+str(-b/(2*a+0.0))+ " - "+D), ("x="+str(-b/(2*a+0.0))+" + "+D)
###############################################################################################
def Second_Law():
    
    u=int(input("Enter coeffient of u\n"))
    a=int(input("Enter coeffient of a\n"))
    t=int(input("Enter coeffient of t\n"))
    
    return ("Distance covered is: "+str(u*t + a*t*t/2)+" meters")
    
    

    
###############################################################################################
def CSVOPENER():
    import csv
    
    with open("/home/deola/Documents/CKD/mydata_Median_Normalized_CKD.csv", "r") as csvfile:
        read_csv=csv.reader(csvfile)
        next(read_csv)
        read_csv=list(read_csv)
        
        result=list()
        
        for row in read_csv:
            result.append(row)
    print(result)
#################################################################################################
    
if __name__=="__main__":
   #print( Bubblesort(arr1))
   MergeSearch(arr1, 22)
   #print (Mergesort(arr1))
   #print (LinearSearch(arr1, 200))
   #MergeSearch(arr1, 9)
   #print(Quicksort(arr1))
   #NN()
   #NNN()
   #print(Recur(256, 10))
   #print(Quadratic())
   #print(Second_Law())
   #CSVOPENER()
