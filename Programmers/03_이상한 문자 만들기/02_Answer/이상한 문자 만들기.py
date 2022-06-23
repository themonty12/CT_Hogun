s = "abc abc abc "

answer = ''

for txt in s.split():
    for i in range(len(txt)):
        if (i % 2) == 1:
           answer += txt[i].lower()
        else:
           answer += txt[i].upper()
    answer += ' '
print(answer[:-1])

        
        
