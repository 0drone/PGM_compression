#!/usr/bin/env python
import numpy as np
import math
import cv2
data=cv2.imread('baboon.pgma',-1)

def flat(arr):
    return np.array(arr).flatten()

#Flatten before entering findVariance
def findVariance(arr):
    total=0
    for i in arr:
        total+=i
    average=(total/len(arr))
    arr2=[]
    for i in arr:
        arr2.append((i-average)*(i-average))
    result=0
    for i in arr2:
        result+=i
    result=result/(len(arr)-1)
    return result


def findAverage(arr):
    total = 0
    for i in arr:
        total += i
    average = (total / len(arr))
    return average


def homogenize(arr):
    final = []
    if(len(arr)==1):
        return arr[0]
    replacement=math.floor(findAverage(flat(arr)))

    for i in range(0,len(arr)):
        pushArr=[]
        for j in range(0,len(arr[i])):
            pushArr.append(replacement)
        final.append(pushArr)
    print(final)
    return final

def quadTree(arr,threshold):

    if (len(arr)==1):
        return arr
    if((findVariance(flat(arr))<=threshold)):
        return homogenize(arr)
    midHorizontal=math.floor(len(arr[0])/2)
    midVertical=math.floor(len(arr)/2)

    arr1=[]
    for i in range(0,midVertical):
        pushArr = []
        for j in range(0,midHorizontal):
            pushArr.append(arr[i][j])
        arr1.append(pushArr)

    arr1=quadTree(arr1,threshold)

    arr2=[]
    for i in range(0, midVertical):
        pushArr = []
        for j in range(midHorizontal,len(arr[i])):
            pushArr.append(arr[i][j])
        arr2.append(pushArr)

    arr2 = quadTree(arr2, threshold)

    arr3=[]
    for i in range(midVertical,len(arr)):
        pushArr = []
        for j in range(0,midHorizontal):
            pushArr.append(arr[i][j])
        arr3.append(pushArr)

    arr3 = quadTree(arr3, threshold)

    arr4=[]
    for i in range(midVertical,len(arr)):
        pushArr = []
        for j in range(midHorizontal,len(arr[i])):
            pushArr.append(arr[i][j])
        arr4.append(pushArr)

    arr4 = quadTree(arr4, threshold)

    merged=[]
    for i in range (0,midVertical):
        pushArr= []
        pushArr.append(arr1[i])
        pushArr.append(arr2[i])
        newArr=np.array(pushArr).flatten()
        merged.append(newArr.tolist())

    for i in range (0,midVertical):
        pushArr= []
        pushArr.append(arr3[i])
        pushArr.append(arr4[i])
        newArr=np.array(pushArr).flatten()
        merged.append(newArr.tolist())
    return merged


print (data)
data2=data

data2=quadTree(data2,256)
data3=np.array(data2)
cv2.imwrite('baboon256.pgm',data3)
