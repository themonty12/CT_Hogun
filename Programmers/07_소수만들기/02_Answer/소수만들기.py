#소수 판별
def test(n):
    for i in range(2, n):
        if n % i == 0:
            return False 
    return True

li = [1,2,3,4]
temp = []
answer = 0
#각 자리수끼리 중복되지 않게 더한 값을 새 리스트에 추가
#포문 돌리는 시작 범위는 i , i+1 , i+2
for i in range(len(li)):    
    for j in range(i + 1, len(li)):
        for k in range(j + 1, len(li)):
            temp.append(li[i] + li[j] + li[k])
            print("{}+{}+{} = {}".format(li[i], li[j], li[k],li[i] + li[j] + li[k]))
        
#새 리스트를 소수판별함수를 돌려 True가 나오면 answer값에 + 1 하여 결과 도출
for ans in temp:
    if test(ans):
        answer += 1
        print("True, {}".format(ans))
print(answer)

