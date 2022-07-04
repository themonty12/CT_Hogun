dartresult = "1D2S#10S"

newresult = dartresult.replace("S", "^1")
newresult = dartresult.replace("D", "^2")
newresult = dartresult.replace("T", "^3")
newresult = dartresult.replace("#", "*(-1)")

answer = 0

for n in range(1, len(dartresult)):
    if dartresult[n-1].isnumeric() and dartresult[n].isnumeric():
        newresult



print(dartresult)