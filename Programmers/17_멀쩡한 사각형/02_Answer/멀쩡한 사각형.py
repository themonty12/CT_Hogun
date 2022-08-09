import math

w = 8
h = 12
result = 0


if w == h:
    result = w*w-w
else:
    result = w*h
    temp = 0
    for i in range(0,w+1):
        #print(math.ceil((math.floor(i * h/w) - temp)))
        print(math.floor(i * h/w))
        result -= math.ceil((math.floor(i * h/w) - temp))
        temp = math.floor(i * h/w)
print(result)
