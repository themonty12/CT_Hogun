s = "abc abc abc "

answer = ''
#입력받은 문자열을 공백으로 split
for txt in s.split(" "):
    #나뉘어진 문자열의 홀수번째는 소문자로, 짝수번째는 대문자로 변경
    for i in range(len(txt)):
        if (i % 2) == 1:
           answer += txt[i].lower()
        else:
           answer += txt[i].upper()
    answer += ' '
print(answer[:-1])

        
        
