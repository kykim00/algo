board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]
new_board = list(map(list, zip(*board)))
stack= []
answer= 0
for i in moves:
    for j in new_board[i-1]:
        if j > 0:
            stack.append(j)
            new_board[i-1].remove(j)
            break
    if len(stack) >= 2 and stack[-1] == stack[-2]:
        stack.pop()
        stack.pop()
        answer += 2
print(answer)