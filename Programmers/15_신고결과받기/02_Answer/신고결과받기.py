id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
#신고 먹은 횟수 카운트용 리스트
li1= list(0 for i in range(len(id_list)))
#한번신고했던 list
use_list = [[] for i in range(len(id_list))]

for i in report:
    print(id_list.index(i.split(" ")[0]))
    txt = i.split(" ")[0]
    id_index = id_list.index(i.split(" ")[0])
    #신고한애는 use_list에 기록 
    use_list[id_index].append(i.split(" ")[1])
    #첨신고당한애만 카운트
    if not txt in use_list[id_index]:
        li1[id_index] +=1
print(li1)
print(use_list)
for i in range(0,len(li1)):
    if li1[i] >= 2:
        print(id_list[i])
        
    

