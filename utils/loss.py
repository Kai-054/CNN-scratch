import math 
from typing import Optional, Union
import torch 
from torch import Tensor 


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

def cross_entropy():
    softmax_output = [0.7, 0.1, 0.2]
    target_output = [1, 0 , 0]
    save = []
    for x , y in zip(softmax_output, target_output):
        cross_entropy_loss =  -y*math.log(x)
        save.append(cross_entropy_loss)
        print(f"Cross Entropy Loss for each: {cross_entropy_loss}")
    total_loss = sum(save)
    average_loss = total_loss /len(save)
    return print(f"Cross Entropy Loss: {total_loss} --- Average Loss: {average_loss}")

test = cross_entropy()
print(test)


    
