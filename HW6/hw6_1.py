def candy_crush(board):
    if not board or not board[0]:
        return board

    m, n = len(board), len(board[0])
    crushed = True

    while crushed:
        crushed = False

        # Check for horizontal crushes
        for i in range(m):
            for j in range(n - 2):
                if abs(board[i][j]) == abs(board[i][j+1]) == abs(board[i][j+2]) != 0:
                    board[i][j] = board[i][j+1] = board[i][j+2] = -abs(board[i][j])
                    crushed = True

        # Check for vertical crushes
        for i in range(m - 2):
            for j in range(n):
                if abs(board[i][j]) == abs(board[i+1][j]) == abs(board[i+2][j]) != 0:
                    board[i][j] = board[i+1][j] = board[i+2][j] = -abs(board[i][j])
                    crushed = True

        # Drop candies
        if crushed:
            for j in range(n):
                bottom = m - 1
                for i in range(m - 1, -1, -1):
                    if board[i][j] > 0:
                        board[bottom][j] = board[i][j]
                        bottom -= 1
                for i in range(bottom, -1, -1):
                    board[i][j] = 0

    return board

def input_board():
    while True:
        try:
            print("請輸入board（格式如：[[110,5,112,113,114],[210,211,5,213,214],...]）：")
            input_str = input().strip()
            # 移除開頭和結尾的方括號
            input_str = input_str[1:-1]
            # 分割每一行
            rows = input_str.split('],')
            board = []
            for row in rows:
                # 移除開頭的方括號和結尾的方括號（如果有）
                row = row.strip('[').strip(']').strip()
                # 分割數字，移除空格，並轉換為整數
                board.append([int(x.strip()) for x in row.split(',') if x.strip()])
            
            # 檢查board是否為空或者是否所有行的長度相等
            if not board or any(len(row) != len(board[0]) for row in board):
                raise ValueError("無效的board格式")
            
            return board
        except ValueError as e:
            print(f"錯誤：{e}。請重新輸入。")
# 主程式
while True:
    board = input_board()
    print("\n輸入的board：")
    for row in board:
        print(row)
    
    result = candy_crush(board)
    print("\n消除後的board：")
    for row in result:
        print(row)
    
    play_again = input("\n是否要再玩一次？(y/n): ").lower()
    if play_again != 'y':
        break

print("謝謝使用！")
