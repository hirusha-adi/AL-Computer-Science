# TASK 13.08

1. Write pseudocode to save the array data from Task 13.06 to a text "file.txt".

- Python Implementation

```python
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

for row in range(3):
    for col in range(3):
        board[row][col] = ' '

board[0][0] = 'O'
board[1][1] = 'X'

filename = 'board_data.txt'  # Specify the desired filename
with open(filename, 'w') as file:
    for row in board:
        file.write(' '.join(row) + '\n')

```

- Pseudocode Implementation

```
DECLARE board: ARRAY[0:2,0:2] OF CHAR

FOR row <- 0 TO 2
    FOR column <- 0 TO 2
        board[row, column] = ' '
    NEXT column
NEXT row

board[0,0] = 'O'
board[1,1] = 'X'

OPENFILE "file.txt" FOR WRITE

row <- 0
column <- 0
FOR row <- 0 TO 2
    FOR column <- 0 TO 2
        WRITEFILE ""file.txt".txt", board[row][column]
        IF column < len(board[row]) - 1
        THEN
            WRITEFILE "file.txt". ' '
        ENDIF
    NEXT column
    WRITEFILE "file.txt", '\n' // write a  new line to the "file.txt"
NEXT row
```

2. Write pseudocode to read the values stored in the text "file.txt" back into the board array

- Python Implementation

```python
def read_board_from_file(filename):
    with open(filename, 'r') as file:
        board = []
        for line in file:
            row = line.strip().split(' ')
            board.append(row)
        return board

filename = 'board_data.txt'  # specify the filename used to save the board data
board = read_board_from_file(filename)

# print and verify
for row in board:
    print(row)

```

- Pseudocode Implementation

```
do we have a .split() like function in pseudocode?
```
