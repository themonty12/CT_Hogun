new_id = "...!@BaT#*..y.abcdefghijklm"
new_id = new_id.lower()

answer = ""


for t in new_id:
    if not (t.isalpha() or t.isnumeric()):
        if not( t == "-" or t == "_" or t == "."):
            new_id = new_id.replace(t,"")
    

answer = new_id
while not answer.find(".."):
    answer = answer.replace("..",".")

while (answer[0] == '.'):
    if len(answer) <= 1:
        answer = "aaa"
    else:
        if answer[0] == ".":
            answer = answer[1:]

if len(answer) > 15:
    answer = answer[:15]

while (answer[-1] == '.'):
    if answer[-1] == ".":
        answer = answer[:len(answer)-1]

if answer == '':
    answer == "aaa"

while len(answer) < 3:
    answer += answer[-1]
    

print(answer)    