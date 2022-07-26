def solution(a, n):
    answer = ''
    #각각의 문자열에대해서 반복
    for s in a:
        #공백이면 answer에 공백 추가
        if s == " ":
            answer += " "
            continue
        #문자의 아스키코드 숫자에 + n
        #+n한 값이 90을 넘어가면 -26 (대문자)
        if 65 <= ord(s) and ord(s) <= 90:
            if ord(s)+n > 90:
                answer += chr(ord(s)+n - 26)
            else:
                answer += chr(ord(s)+n)
        #+n한 값이 122을 넘어가면 -26 (소문자)
        else:   
            if ord(s)+n > 122:
                answer += chr(ord(s)+n - 26)
            else:
                answer += chr(ord(s)+n)
            
    return answer