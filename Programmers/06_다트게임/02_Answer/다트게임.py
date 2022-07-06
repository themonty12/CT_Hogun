def solution(dartresult):
    answer = 0
    
    new_list=[]
    #문자열을 돌면서 숫자인지 아닌지 판별
    for n in range(0, len(dartresult)):
        #숫자면 new_list에 추가, 문자열에 10이 들어가 있을 때 예외 처리 
        if dartresult[n].isnumeric():                        
            if dartresult[n] == "1" and dartresult[n+1] == "0":
                new_list.append(10)
            else:
                if not(dartresult[n] == "0" and dartresult[n-1] == "1"):           
                    new_list.append(int(dartresult[n]))
        #문자가 숫자가 아닐 때 각 문자 별로 new_list의 item에 계산식 처리
        else:
            # S, D, T는 각 문자별로 제곱
            if dartresult[n] == "S":
                new_list[-1] = new_list[-1] ** 1        
            if dartresult[n] == "D":
                new_list[-1] = new_list[-1] ** 2
            if dartresult[n] == "T":
                new_list[-1] = new_list[-1] ** 3
            # #문자는 가장 마지막 item에 -1 곱
            if dartresult[n] == "#":
                 new_list[-1] = new_list[-1] * (-1)
            # *문자는 가장 마지막 문자열에 x2
            if dartresult[n] == "*":
                new_list[-1] = new_list[-1] * 2
                #만약 리스트의 count가 1 보다 크면 리스트 [-2]에도 x2
                if len(new_list) > 1:
                    new_list[-2] = new_list[-2] * 2
            #리스트의 모든 아이템 합치기
    for i in new_list:
        answer += i
        
    return answer
