N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

per = []
sort = {}
answer =[]

for j in range(1, N+1):
    #리스트가 0이면 continue, 실패율은 0 
    if len(stages) == 0 :
        per.append(0)
        continue
    print("stages item : {}".format(len(stages)))
    print("li[j] : {}".format(stages.count(j)))
    #머문 사람 수 / 남은 스테이지 수 
    per.append(stages.count(j)/ len(stages))
    if not stages.count(j) == 0:
        #계산했던 스테이지는 리스트에서 제거
        remove_set = [j]
        stages = [itm for itm in stages if itm not in remove_set]
        print(stages)
            
 #실패율과 스테이지 dict으로 묶기              
for i in range(0, len(per)):
    sort[i+1] = per[i]
    
print(sort)
#dict정렬
temp = sorted(sort.items(), key=lambda x:x[1], reverse = True)
print(temp)
#실패율로 스테이지 정렬
for itm in range(0, len(temp)):
    answer.append(temp[itm][0])

print(answer)
