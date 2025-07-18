import math 
from typing import Optional, Union

def sigmoid(x):
    f_sigmoid = 1/1+math.exp(-x)
    return f_sigmoid

def relu(x):
    if x  > 0:
        return x
    else:
        return 0

def tanh(x):
    f_tanh = (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))
    return f_tanh

def softmax():
    input = [10, 25, 63 ,23 ,90, 15]
    save_numerator = []
    save_denominator = []
    
    for i in input:
        save_numerator.append(pow((math.e), i))
        print("Save value:", save_numerator)
    
    for i in save_numerator:
        save_denominator.append(i/sum(save_numerator))
        print("Denominator:", save_denominator)
        rs_softmax = sum(save_denominator)
    return print (f"softmax: {rs_softmax}")
        
# test = softmax()
# print(test)

def cross_entropy: 
