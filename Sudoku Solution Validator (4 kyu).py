def validSolution(board):
    temp = [board[i][k] for k in range(0,9) for i in range(0,9)]
    columns = [temp[i:i+9] for i in range(0, 81, 9)]
    temp = [board[i][0:3] for i in range(0,9)]+[board[i][3:6] for i in range(0,9)]+[board[i][6:9] for i in range(0,9)]
    blocks = [[k for i in temp for k in i][i:i+9] for i in range(0,81,9)]
    for i in range(1, 10):
        for k in board:
            if 0 in k:
                return False
            if k.count(i)>1:
                return False
        for k in columns:
            if k.count(i)>1:
                return False
        for k in blocks:
            if k.count(i)>1:
                return False
    return True


validSolution([[1, 2, 3, 4, 5, 6, 7, 8, 9],
               [2, 3, 4, 5, 6, 7, 8, 9, 1],
               [3, 4, 5, 6, 7, 8, 9, 1, 2],
               [4, 5, 6, 7, 8, 9, 1, 2, 3],
               [5, 6, 7, 8, 9, 1, 2, 3, 4],
               [6, 7, 8, 9, 1, 2, 3, 4, 5],
               [7, 8, 9, 1, 2, 3, 4, 5, 6],
               [8, 9, 1, 2, 3, 4, 5, 6, 7],
               [9, 1, 2, 3, 4, 5, 6, 7, 8]])
