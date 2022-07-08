absolutes = [4,7,12]
signs = [True,False,True]

answer = 0
#absolutes 리스트를 돌면서
for i in range(0,len(absolutes)):
    #같은 인덱스의 signs 리스트의 아이템이 True이면 양 False면 음
    if signs[i]:
        answer += absolutes[i]
    else:
         answer += absolutes[i] *(-1)
         #Answer에 결과 더하기
print(answer)
