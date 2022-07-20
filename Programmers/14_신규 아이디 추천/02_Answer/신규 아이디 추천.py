new_id = "123_.def"
new_id = new_id.lower()

answer = ''
for t in new_id:
    if not (t.isalpha() or t.isnumeric()):
        if not( t == "-" or t == "_" or t == "."):
            new_id = new_id.replace(t,"")
    
for i in range(0,len(new_id)):
    if new_id[0] == ".":
        new_id = new_id[1:]
    if new_id[-1] == ".":
        new_id = new_id[:len(new_id)-1]
while len(new_id) < 3:
    new_id += new_id[-1]
if new_id == '':
    new_id == "aaa"
answer = new_id
print(answer)    