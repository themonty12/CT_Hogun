number = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
result = ""
rh = 12
lh = 10
#리스트 돌면서 왼손 오른손 판별
for i in number:
    if i == 1 or i == 4 or i == 7:
        result += "L"
        lh = i
    elif i == 3 or i == 6 or i == 9:
        result += "R"
        rh = i
    else:
        if abs(i - rh) > abs(i - lh):
            result += "L"
            lh = i
        elif abs(i - rh) < abs(i - lh):
            result += "R"
            rh = i
        #가운데 숫자일때 가까운 손 비교
        else:
            if i == 0 :
                i = 11
            if find_length(i, lh) > find_length(i, rh):
                result += "R"
            elif find_length(i, lh) < find_length(i, rh):
                result += "L"
            else:
                result += hand[0].upper()


return result

#가까운 손 비교 함
def find_length(x,y):
    if abs(x-y) == 1 or abs(x-y) == 3:
        return 1
    elif abs(x-y) == 2 or abs(x-y) == 4 or abs(x-y) == 6:
        return 2
    elif abs(x-y) == 5 or abs(x-y) == 7:
        return 3
    else:
        return 4