n=9
answer = 0
first_n = []
#3으로 나뉘지 않을 때 까지 나누기
while n >= 3:
    first_n.append(int(n%3))
    n=n/3
#나머지는 리스트에 저장
first_n.append(int(n))

#문자열에 식 삽입
for i in range(len(first_n)):

    answer +=((3 ** (len(first_n)- i-1) *first_n[i]))
print(answer)
    
