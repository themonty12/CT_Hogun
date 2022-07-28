number = [0,5,2,4,4,6,4,5,5,5,5,5]	
hand = "left"
result = ""
rh = 12
lh = 10

def find_length(x,y):
    if abs(x-y) == 1 or abs(x-y) == 3:
        return 1
    elif abs(x-y) == 2 or abs(x-y) == 4 or abs(x-y) == 6:
        return 2
    elif abs(x-y) == 5 or abs(x-y) == 7 or abs(x-y) == 9:
        return 3
    elif abs(x-y) == 0:
        return 0
    else:
        return 4
    
#리스트 돌면서 왼손 오른손 판별
for i in number:
    if i == 1 or i == 4 or i == 7:
        result += "L"
        lh = i
    elif i == 3 or i == 6 or i == 9:
        result += "R"
        rh = i
    else:
        
        #가운데 숫자일때 가까운 손 비교
        if i == 0 :
              i = 11

        if find_length(i, lh) > find_length(i, rh):
            rh = i
            result += "R"
        elif find_length(i, lh) < find_length(i, rh):
            lh = i
            result += "L"
        else:
           result += hand[0].upper()
           if hand[0].upper() == "L":
                   lh = i
           else:
                   rh = i                      


print( result)

#가까운 손 비교 함

