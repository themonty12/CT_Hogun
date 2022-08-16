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
        result -= math.ceil((math.ceil(i * h/w) - temp))
        temp = math.floor(i * h/w)

print(result)

