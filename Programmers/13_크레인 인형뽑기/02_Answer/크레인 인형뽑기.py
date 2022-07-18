board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
answer = 0
moves = [1,5,3,5,1,2,1,4]
result = []
# moves 값따라서 board 내용 확인
for x in moves:
    for i in range(len(board[x-1])-1, -1,-1):  
        if not board[x-1][i] == 0:
            result.append(board[x-1][i])
            board[x-1][i] = 0

            break
#중복되면 answer에 사라진 숫자 개수만큼 더하기
switch = True       
while switch == True:
    for i in range(len(result)-1,0,-1):

        if result[i] == result[i-1]:     
            answer += 2
            result.remove(i)
            result.remove(i)
            switch = True
            
            break
        else:
            switch = False
            
    if len(result) < 2:
        switch = False

print(answer)
    
            
    
       
        
    
    
