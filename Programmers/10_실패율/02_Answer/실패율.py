N = 5
stages = [2,1,2,6,2,4,3,3]
li = []
per = []
answer = []
#각 스테이지 머문 사람 수 찾기
for i in range(N+1):
    li.append(stages.count(i+1))
print(li)
#머문 사람 수 / 총 스테이지 수 
for j in range(0, len(li)):
    per.append(li[j] / len(stages))
    if not li[j] == 0:
        for itm in stages:
            if itm == (j+1):
                stages.remove(itm)
    print(stages)
print(per)
