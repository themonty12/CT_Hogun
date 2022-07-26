id_list = ["muzi", "frodo", "apeach", "neo"]	
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	
#신고 먹은 횟수 카운트용 리스트
k = 2
li1= list(0 for i in range(len(id_list)))
#한번신고했던 list
use_list = [[] for i in range(len(id_list))]

answer = list(0 for i in range(len(id_list)))
for i in report:
    #리포트 리스트를 띄어쓰기로 분리
    txt = i.split(" ")[0]
    id_index = id_list.index(i.split(" ")[0])
    
    #뒤에 있는 문자가 신고당한 id일때 중복신고 방지 리스트에 추가
    #이미 추가되어있는 아이디는 제외
    if not i.split(" ")[1] in use_list[id_index]:
        use_list[id_index].append(i.split(" ")[1])
        #신고당한 횟수 리스트에 추가
        li1[id_list.index(txt)-1] +=1

#중복방지 리스트와 아이디리스트 비교해서
print(li1)
for i in range(len(use_list)):
    #중복방지 리스트에 있는 아이디가 경고횟수 k 이상이면 answer동일한 인덱스에 +1
    for j in range(len(li1)):
        if li1[j]>=k:
            print(id_list[j])
            
            if id_list[j] in use_list[i]:
                print(i)
                answer[i] += 1
                
print(answer)
