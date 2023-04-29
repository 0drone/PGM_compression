import numpy as np
import math
import cv2

'''
data=cv2.imread('baboon.pgma',-1)
print(data)

data2=data
print(data2)
write('baboon3.pgm',data2)
'''
'''
from gpu import *

gpu1=Gpu(1300,10,15)
print(gpu1.cost)

def translate(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation+="g"
        else:
            translation+=letter
    return translation

print(translate("dog"))
'''
def flat(arr):
    return np.array(arr).flatten()

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

'''
def flattenArray(arr):
    result=[]
    for i in arr:
        print(arr[i])
        for j in i:
            result.apend(j)
    return result
arr1=np.array([[1,2,3],[1,2,3]])
print(arr1.flatten())

'''

arr=[[1,1,3,4,5,6,7,8],
     [1,1,3,4,5,6,7,8],
     [1,2,3,4,5,6,7,8],
     [1,2,3,4,5,6,7,8],
     [9,10,11,12,13,14,15,16],
     [9,10,11,12,13,14,15,16],
     [9,10,11,12,13,14,15,16],
     [9,10,11,12,13,14,15,250]]

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

    return final


def quadTree(arr,threshold):

    if((findVariance(flat(arr))<=threshold) or (len(arr)==1)):
        return homogenize(arr)
    midHorizontal=math.floor(len(arr[0])/2)
    midVertical=math.floor(len(arr)/2)
    #IF threhold
    #THEN homogenize
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
    print(merged)
    #merge


    return merged

print(quadTree(arr,40))
print (result)


