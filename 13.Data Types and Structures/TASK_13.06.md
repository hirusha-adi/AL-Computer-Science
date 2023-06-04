# TASK 13.06

1. Declare a 2D array to store the board data for the game Noughts and Crosses. The
   empty squares of the board are to be represented by a space. Player A’s counters
   are to be represented by “O”. Player B’s counters are to be represented by “X”.

2. Initialise the array to start with each square being empty.

3. Write a statement to represent player A placing their counter in the top left square.

4. Write a statement to represent player B placing their counter in the middle square.

```
DECLARE board: ARRAY[0:2,0:2] OF CHAR

FOR row <- 0 to 2
    FOR column <- 0 to 2
        board[row, column] = ' '
    NEXT column
NEXT row

board[0,0] = 'O'
board[1,1] = 'X'
```

or in Python

```python
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

for row in range(3):
    for col in range(3):
        board[row][col] = ' '

board[0][0] = 'O'
board[1][1] = 'X'
```
