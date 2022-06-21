def solution(n):
    txt = str(n)
    n_txt = ""
    i = 1
    while i <= len(txt):
        n_txt += txt[-1]
        i += 1
        if i > len(txt):
            break
    
    
    answer = []
    
    return answer