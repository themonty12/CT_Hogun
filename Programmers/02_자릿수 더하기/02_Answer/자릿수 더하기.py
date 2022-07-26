def solution(n):
    #숫자열 문자 변경
    txt = str(n)
    answer = 0
    #각 자리의 문자를 숫자로 변경하여 answer에 더하기
    for i in range(len(txt)):
        answer += int(txt[i])
  
    return answer