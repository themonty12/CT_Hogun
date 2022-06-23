def solution(n):
    #입력받은 숫자를 문자로 변환
    txt = str(n)
    answer = []
    i = 1
    #변환한 문자열 길이만큼 반복
    while i <= len(txt):
        #return할 리스트에 문자열 뒷 열부터 append
        answer.append(int(txt[-i]))
        i += 1
       
    
    return answer