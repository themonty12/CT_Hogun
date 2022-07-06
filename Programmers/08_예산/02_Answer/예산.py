li = [1,2,3,4,5,6,7,8,9,10]
budget = 44

#기존 리스트 임시 리스트에 복사
new_li = li.copy()

#리스트 돌면서 각 인덱스를 하나씩 뺀값을 new_li에 반영
for i in range(0, len(li)):
    print(i)
    new_li.remove(li[i])
    print(li)
    print(new_li)
    #해당 위치에 new_li의 sum과 budget 비교 코드 추가 예정
    new_li = li.copy()