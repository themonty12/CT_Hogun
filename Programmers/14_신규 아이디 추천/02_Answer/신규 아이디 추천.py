new_id = "...!@BaT#*..y.abcdefghijklm"

#소문자로 변경
new_id = new_id.lower()

answer = ""

#영어, 숫자 특정 문자가 아니면 삭제
for t in new_id:
    if not (t.isalpha() or t.isnumeric()):
        if not( t == "-" or t == "_" or t == "."):
            new_id = new_id.replace(t,"")
    
answer = new_id
#. 두개 이상 연속으로 나오면 하나만 남김
while not answer.find("..")== -1:
    answer = answer.replace("..",".")

#앞에 온점이 나오면 시작
while (answer[0] == '.'):
    #문자가 한글자 이하로 줄면 aaa로변경
    if len(answer) <= 1:
        answer = "aaa"
    #앞에 온점이 나오면 삭제
    else:
        if answer[0] == ".":
            answer = answer[1:]
#문자길이 15넘어가면 뒤에 문자 제거
if len(answer) > 15:
    answer = answer[:15]
#뒤에 온점이 나오면 삭제
while (answer[-1] == '.'):
    if answer[-1] == ".":
        answer = answer[:len(answer)-1]
#문자없으면 aaa
if answer == '':
    answer == "aaa"
#문자 길이가 3이하면 마지막 문자 반복
while len(answer) < 3:
    answer += answer[-1]
    

print(answer)    
