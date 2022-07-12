N = 5
stages = [2,1,2,6,2,4,3,3]

per = []
sort = {}

#머문 사람 수 / 총 스테이지 수 
for j in range(1, N+1):
    print("stages item : {}".format(len(stages)))
    print("li[j] : {}".format(stages.count(j)))
    per.append(stages.count(j)/ len(stages))
    if not stages.count(j) == 0:
        remove_set = [j]
        stages = [itm for itm in stages if itm not in remove_set]
        print(stages)
            
               
for i in range(0, len(per)):
    sort[i+1] = per[i]
    
print(sort)

temp = sorted(sort.items(), key=lambda x:x[1], reverse = True)
print(temp)
for itm in range(0, len(temp)):
    answer = temp[itm]
print(answer)
