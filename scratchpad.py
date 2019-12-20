import numpy as np

def softmax(x):

    x_exp = np.exp(x)
    print(x_exp.shape)


    x_sum = np.sum(x_exp, axis=1, keepdims=True)
    print(x_sum)
    print(x_sum.shape)

    s = x_exp / x_sum
    print(s.shape)

    return s

x = np.array([
    [1,2,3,4],
    [5,6,7,8]
])
# print(x.shape)

print(softmax(x))