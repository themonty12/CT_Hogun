n=45

first_n = []
#3으로 나뉘지 않을 때 까지 나누기
while n > 3:
    first_n.append(int(n%3))
    n=n/3
#나머지는 리스트에 저장
first_n.append(int(n))
semi_ans = ""
answer = 0
#리스트 각 문자를 문자열로 변경(삭제)
for i in first_n:
    semi_ans += str(i)
#문자열에 식 삽입
for i in range(len(semi_ans)):
    answer +=((3 ** (len(semi_ans)- i-1) *int(semi_ans[i])))
print(answer)
    
