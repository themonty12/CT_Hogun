
def remove_list(li , budget, count):
    new_li = li.copy()
    for i in range(0, len(li)):
        new_li.remove(li[i])
        #리스트 다 더한값이 예산이랑 같으면 리스트 아이템 수가 answer
        if sum(new_li) == budget:
            return len(new_li)
        new_li = li.copy()
    remove_list(li, budget, count)
            
            
        
        

                   

li = [1,2,3,4,5,6,7,8,9,10]
budget = 44
answer = 0
#기존 리스트 임시 리스트에 복사
new_li = li.copy()

#리스트 돌면서 각 인덱스를 하나씩 뺀값을 new_li에 반영
if budget == sum(li):
    answer = len(li):
else:
    for i in range(0, len(li)):
        print(i)
        for j in range(0, i):
            
        new_li.remove(li[i])
        print(new_li)
           #해당 위치에 new_li의 sum과 budget 비교 코드 추가 예정
        if budget == sum(new_li):
            answer = len(new_li)
            break
        new_li = li.copy()
    

        
