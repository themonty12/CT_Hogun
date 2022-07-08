li = [1,3,2,5,4]
budget = 9
answer = 0
count = 0
#리스트 작은수부터 정렬
li.sort()
#리스트 돌면서 count가 예산을 초과하지 않으면 count += 1 
for i in range(0, len(li)):
    count += li[i]
    if budget >= count:
        answer += 1
    #count가 넘어가면 탈출
    else:
        break

    
print(answer)
        
