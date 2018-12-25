#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 11:11:57 2018

@author: deola
"""

##################################################################################################

arr1=[3,2,1,200,4,7,8,9]


def Bubblesort(arr):
    ''' Algorithm for bubble sort'''
    for i in range(0,len(arr)):
        for j in range(len(arr)-1,i,-1):
            print i,j
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1], arr[j]
    return arr
################################################################################################
def Mergesort(arr):
    '''Algorithm for merge sort'''
    i,j,k=0,0,0
    
    if len(arr)<=1:
        return "Done"
    
    else:
        mid=len(arr)/2
        arrLeft=arr[mid:]
        arrRight=arr[:mid]
        print arrRight, arrLeft
        Mergesort(arrLeft)
        Mergesort(arrRight)
################################################################################################        
        #while i <len(arrLeft) and j< len(arrRight):
def LinearSearch(arr, obj):
    '''Searching for a definite object in an array'''
    for element in arr:
        #print element
        if element==obj:
            print True
        else:
            print False
##############################################################################################
def MergeSearch(arr, obj):
    if len(arr)<=1:
        return "Done"
    
    else:
        mid=len(arr)/2
        arrLeft=arr[mid:]
        arrRight=arr[:mid]
        print arrRight, arrLeft
        
        #Searching the divided array
        LinearSearch(arrLeft, obj)
        LinearSearch(arrRight, obj)
        
        #Recurively dividing
        
        Mergesort(arrLeft)
        Mergesort(arrRight)
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

        
##################################################################################################


if __name__=="__main__":
   #print( Bubblesort(arr1))
   #print (Mergesort(arr1))
   #print (LinearSearch(arr1, 0))
   print(Quicksort(arr1))
