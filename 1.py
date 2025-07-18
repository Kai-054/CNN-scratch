math_grades = [85, 90, 78, 92, 88]
eng_grades = [80, 85, 88, 90, 95]
literature_grades = "82, 87, 85, 89, 91"
avg = []
# for i in range(len(math_grades)):
#     avg.append((math_grades[i]+ eng_grades[i])/2)
# print(avg)

# for i,j,k in zip(math_grades, eng_grades, avg):
#     # print(f"Math: {i}, English: {j}, Average: {k}")

import numpy as np 
a = np.array([math_grades])
b = np.array([eng_grades])
c = (a+b)/2
# print(c)

grades = np.array([[7,8,6],
                   [3,1,2], 
                   [5,4,6]])

scorce = np.array([3, 4, 5])
result = (grades + scorce)
print(grades.shape)
print(scorce.shape)
print (grades + scorce)

import os
import sys

def myFunc(x):
    return x * 2

print(myFunc(4))
