def solution(dartresult):
    answer = 0
    
    new_list=[]

    for n in range(0, len(dartresult)):

        if dartresult[n].isnumeric():                        
            if dartresult[n] == "1" and dartresult[n+1] == "0":
                new_list.append(10)
            else:
                if not(dartresult[n] == "0" and dartresult[n-1] == "1"):           
                    new_list.append(int(dartresult[n]))
        else:
            if dartresult[n] == "S":
                new_list[-1] = new_list[-1] ** 1        
            if dartresult[n] == "D":
                new_list[-1] = new_list[-1] ** 2
            if dartresult[n] == "T":
                new_list[-1] = new_list[-1] ** 3
            if dartresult[n] == "#":
                 new_list[-1] = new_list[-1] * (-1)
            if dartresult[n] == "*":
                new_list[-1] = new_list[-1] * 2
                new_list[-2] = new_list[-2] * 2
    for i in new_list:
        answer += i
        
    return answer