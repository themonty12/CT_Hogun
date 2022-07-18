s = "23four5six7"
#특정 영문을 숫자로 변경
s = s.replace("zero", "0")
s = s.replace("one", "1")
s = s.replace("two", "2")
s = s.replace("three", "3")
s = s.replace("four", "4")
s = s.replace("five", "5")
s = s.replace("six", "6")
s = s.replace("seven", "7")
s = s.replace("eight", "8")
s = s.replace("nine", "9")
#문자를 숫자로 변경
answer = eval(s)
print(answer)
