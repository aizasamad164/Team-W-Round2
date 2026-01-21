def solve_sudoko(board):
    if not is_board_valid(board):
        return False

    empty_cell = find_empty(board)

    if empty_cell is None:
        return True

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoko(board) is True:
                return True

            board[row][col] = 0

    return False

# Board Validation
def is_board_valid(board):
    # Check all pre-filled cells in the board
    for i in range (9):
        for j in range (9):
            if board[i][j] != 0:
                num = board[i][j]
                
                # Check row for conflicts (excluding current cell)
                for col in range (9):
                    if col != j and board[i][col] == num:
                        return False
                
                # Check column for conflicts (excluding current cell)
                for row in range (9):
                    if row != i and board[row][j] == num:
                        return False
                
                # Check 3×3 box for conflicts (excluding current cell)
                box_row = i // 3  # Integer division
                box_col = j // 3  # Integer division
                
                for r in range (box_row * 3, (box_row * 3) + 2):
                    for c in range (box_col * 3, (box_col * 3) + 2):
                        if (r != i or c != j) and board[r][c] == num:
                            return False
    
    # All pre-filled cells are valid
    return True


# move validation
def is_valid (board, num, position):
    row, col = position

    for j in range(9):
        if board[row][j] == num and j != col:
            return False

    for i in range(9):
        if board[i][col] == num and i != row:
            return False

    box_row = row // 3
    box_col = col // 3

    for i in range (box_row * 3, (box_row * 3) + 2):
        for j in range (box_col * 3, (box_col * 3) + 2):
            if board[i][j] == num and (i, j) != position:
                return False

    return True

# Helper Functions
def find_empty(board):
    for i in range (9):
        for j in range (9):
            if board[i][j] == 0:
                return (i, j)
    
    return None

        
def print_board(board):
    for i in range (9):
        
        if i % 3 == 0 and i != 0:
            print("---------------------")
        
        for j in range (9):
            # Print vertical separator after every 3 columns
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            
            # Print cell value (dot for empty)
            if board[i][j] == 0:
                print(". ", end="")
            else:
                print(board[i][j], " ", end="")
        
        print()  # Move to next row
     

# Main Execution Flow
unsolved_sudoku = [[0, 4, 0, 0, 0, 0, 0, 0, 7],
                   [0, 0, 6, 0, 0, 0, 8, 0, 0],
                   [0, 0, 0, 3, 0, 4, 1, 0, 0],
                   [8, 0, 0, 7, 1, 0, 0, 0, 0],
                   [7, 0, 0, 9, 0, 0, 0, 0, 0],
                   [5, 6, 2, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 7, 0, 5, 2],
                   [0, 0, 0, 0, 2, 0, 0, 0, 0],
                   [0, 8, 0, 0, 5, 0, 0, 6, 0]]

for i in range(9):
   for j in range(9):
       unsolved_sudoku[i][j] = int(input())

print("Unsolved Sudoku:")
print_board(unsolved_sudoku)

if solve_sudoko(unsolved_sudoku) is True:
    print("\nSolved Sudoku:")
    print_board(unsolved_sudoku)
else:
    print("\nNo solution exists (puzzle may be invalid or unsolvable).")

    
