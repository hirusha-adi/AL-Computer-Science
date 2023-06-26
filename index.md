# Task 14.01

Use the IDE of your chosen programming language (in future just referred to as ‘your
language’). Type the program statements equivalent to the following pseudocode
(you may need to declare the variable YourName first):
`INPUT "What is your name? " YourName`
`OUTPUT "Have a nice day ", YourName`
Save your program as Example1 and then run it. Is the output as you expected?

```
YourName = input("What is your name?")
print("Have a nice day", YourName)
```

# Task 14.02

1. Look at the identifier tables in Chapter 12 (Tables 12.02 and 12.04 to 12.12). Decide
which data type from your language is appropriate for each variable listed.
2. Write program code to implement the pseudocode from Worked Example 12.01
in Chapter 12.

## Answers

1.  

- Table 12.02

| Identifier | Data Type |
| - | - |
| Miles | int |
| Km | float |

- Table 12.04

| Identifier | Data Type |
| - | - |
| Number1 | float |
| Number2 | float |
| Number3 | float |

- Table 12.05

| Identifier | Data Type |
| - | - |
| BiggestSoFar | float |
| NextNumber | float |

- Table 12.06, Table 12.07, Table 12.08

| Identifier | Data Type |
| - | - |
| BiggestSoFar | float |
| NextNumber | float |
| Counter | int |

- Table 12.09

| Identifier | Data Type |
| - | - |
| SecretNumber | int/float |
| NumberOfGuesses | int |
| Guess | int/float |

- Table 12.11

| Identifier | Data Type |
| - | - |
| NumberOfRows | int |
| NumberOfColumns | int |
| Symbol | str/char |
| RowCounter | int |
| ColumnCounter | int |

- Table 12.12

| Identifier | Data Type |
| - | - |
| MaxNumberOfSymbols | int |
| NumberOfSpaces | int |
| Symbol | str/char |
| NumberOfSymbols | int |

# Task 14.03

Write program code to implement the pseudocode from Worked Example 12.03 in Chapter 12

```
INPUT BiggestSoFar
INPUT NextNumber
IF NextNumber > BiggestSoFar
 THEN
 BiggestSoFar ← NextNumber
ENDIF
INPUT NextNumber
IF NextNumber > BiggestSoFar
 THEN
 BiggestSoFar ← NextNumber
ENDIF
OUTPUT BiggestSoFar
```

```python
BiggestSoFar = input("Input BiggestSoFar: ")
NextNumber = input("Input NextNumber: ")

if NextNumber > BiggestSoFar:
    BiggestSoFar = NextNumber

NextNumber = input("Input NextNumber: ")

if NextNumber > BiggestSoFar:
    BiggestSoFar = NextNumber

print("BiggestSoFar is", BiggestSoFar)
```


# Task 14.04

Write program code to implement the pseudocode from Worked Example 12.02 in Chapter 12.

```
INPUT Number1
INPUT Number2
INPUT Number3
IF Number1 > Number2
    THEN
    // Number1 is bigger
    IF Number1 > Number3
        THEN
        OUTPUT Number1
    ELSE
        OUTPUT Number3
    ENDIF
ELSE
    // Number2 is bigger
    IF Number2 > Number3
        THEN
        OUTPUT Number2
    ELSE
        OUTPUT Number3
    ENDIF
ENDIF
```

```python
Number1 = input("input Number 1: ")
Number2 = input("input Number 2: ")
Number3 = input("input Number 3: ")

if Number1 > Number2:
    if Number1 > Number3:
        print(Number1)
    else:
        print(Number3)
else:
    if Number2 > Number3:
        print(Number2)
    else:
        print(Number3)
```

# Task 14.05

The problem to be solved: the user enters the number of the month and year. The
output is the number of days in that month. The program has to check if the year is a
leap year for February.
The pseudocode solution is:
```
INPUT MonthNumber
INPUT Year
Days ← 0
CASE OF MonthNumber
 CASE 1,3,5,7,8,10,12 : Days ← 31
 CASE 4,6,9,11 : Days ← 30
 CASE 2 : Days ← 28
 If Year MOD 400 = 0
 THEN // it is a leap year
 Days ← 29
 ENDIF
 IF (Year MOD 4 = 0) AND (Year MOD 100 > 0)
 THEN // it is a leap year
 Days ← 29
 ENDIF
 OTHERWISE OUTPUT "Invalid month number"
ENDCASE
OUTPUT Days
```
Write program code to implement the pseudocode above.

```python
def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def get_number_of_days(month_number, year):
    days = 0
    if month_number in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    elif month_number in [4, 6, 9, 11]:
        days = 30
    elif month_number == 2:
        if is_leap_year(year):
            days = 29
        else:
            days = 28
    else:
        print("invlaid month no.")
        return

    return days

# Read input from the user
month_number = int(input("Enter the month no.: "))
year = int(input("Enter the year: "))

# Calculate and display the number of days
number_of_days = get_number_of_days(month_number, year)
if number_of_days is not None:
    print("Number of days:", number_of_days)
```

# Task 14.06

1. Write program code to implement the pseudocode from Worked Example 12.05 in Chapter 12.
2. Write program code to implement the pseudocode from Worked Example 12.08 in Chapter 12.
3. Write program code to implement the pseudocode from Worked Example 12.09 in Chapter 12.

## Answer
1. 
```
INPUT BiggestSoFar
FOR Counter ← 2 TO 10
 INPUT NextNumber
 IF NextNumber > BiggestSoFar
 THEN
 BiggestSoFar ← NextNumber
 ENDIF
NEXT Counter
OUTPUT BiggestSoFar
```

```python
biggest_so_far = int(input("Enter the first number: "))

for counter in range(2, 11):
    next_number = int(input("Enter the next number: "))
    if next_number > biggest_so_far:
        biggest_so_far = next_number

print("The biggest number is:", biggest_so_far)
```

2.

```
RunningTotal ← 0
FOR Counter ← 1 TO 10
 INPUT NextNumber
 RunningTotal ← RunningTotal + NextNumber
NEXT Counter
OUTPUT RunningTotal
Average ← RunningTotal / 10
OUTPUT Average
```

```python
running_total = 0

for counter in range(1, 11):
    next_number = int(input("Enter a number: "))
    running_total += next_number

average = running_total / 10

print("Running Total:", running_total)
print("Average:", average)
```

3.

```
INPUT NumberOfRows
INPUT NumberOfColumns
INPUT Symbol
FOR RowCounter ← 1 TO NumberOfRows
 FOR ColumnCounter ← 1 TO NumberOfColumns
 OUTPUT Symbol // without moving to next line
 NEXT ColumnCounter
 OUTPUT Newline // move to the next line
NEXT RowCounter
```

```python
number_of_rows = int(input("number of rows: "))
number_of_columns = int(input("number of columns: "))
symbol = input("symbol: ")

for row_counter in range(1, number_of_rows + 1):
    for column_counter in range(1, number_of_columns + 1):
        print(symbol, end="")  # Print the symbol without moving to the next line
    print()  # Move to the next line
```


# Task 14.07

1. Write program code to implement the pseudocode from Worked Example 12.04 in Chapter 12.
2. Write program code to implement the first algorithm from Worked Example 12.06 in Chapter 12.

## Answers

1.

```
INPUT BiggestSoFar
Counter ← 1
REPEAT
 INPUT NextNumber
 Counter ← Counter + 1
 IF NextNumber > BiggestSoFar
 THEN
 BiggestSoFar ← NextNumber
 ENDIF
UNTIL Counter = 10
OUTPUT BiggestSoFar
```

```python
biggest_so_far = int(input("Enter the first number: "))
counter = 1

while counter < 10:
    next_number = int(input("Enter the next number: "))
    counter += 1
    if next_number > biggest_so_far:
        biggest_so_far = next_number

print("The biggest number entered is:", biggest_so_far)
```


2.

```
INPUT NextNumber
BiggestSoFar ← NextNumber
WHILE NextNumber <> 0 DO // sequence terminator not encountered
 INPUT NextNumber
 IF NextNumber > BiggestSoFar
 THEN
 BiggestSoFar ← NextNumber
 ENDIF
ENDWHILE
OUTPUT BiggestSoFar
```

```python
next_number = int(input("Enter a number: "))
biggest_so_far = next_number

while next_number != 0:
    next_number = int(input("Enter a number (enter 0 to terminate): "))
    
    if next_number > biggest_so_far:
        biggest_so_far = next_number

print("The biggest number entered is:", biggest_so_far)
```

# Task 14.08

Write program code to implement the second algorithm from Worked Example 12.06 in Chapter 12.

```
INPUT NextNumber
BiggestSoFar ← NextNumber
WHILE NextNumber <> 0 DO // sequence terminator not encountered
 INPUT NextNumber
 IF NextNumber > BiggestSoFar
 THEN
 BiggestSoFar ← NextNumber
 ENDIF
ENDWHILE
OUTPUT BiggestSoFar
```

```python
next_number = int(input("Enter a number: "))
biggest_so_far = next_number

while next_number != 0:
    next_number = int(input("Enter a number (enter 0 to terminate): "))
    
    if next_number > biggest_so_far:
        biggest_so_far = next_number

print("The biggest number entered is:", biggest_so_far)
```

# Task 14.09
1. Write program code to generate 20 random numbers in the range 1 to 10 inclusive.
2. Write program code to implement the pseudocode using a pre-condition loop from Worked Example 12.07 in Chapter 12

## Answers

1. 
```python
import random

random_numbers = []
for _ in range(20):
    random_number = random.randint(1, 10)
    random_numbers.append(random_number)

print("Random Numbers:", random_numbers)
```

2.
```
SecretNumber ← Random
INPUT Guess
NumberOfGuesses ← 1
WHILE Guess <> SecretNumber DO
 IF Guess > SecretNumber
 THEN
 // the player is given the message to input a smaller number
 ENDIF
 IF Guess < SecretNumber
 THEN
 // the player is given the message to input a larger number
 ENDIF
 INPUT Guess
 NumberOfGuesses ← NumberOfGuesses + 1
ENDWHILE
OUTPUT NumberOfGuesses
```

```python
import random

secret_number = random.randint(1, 10)
guess = int(input("Enter your guess: "))
number_of_guesses = 1

while guess != secret_number:
    if guess > secret_number:
        print("Enter a smaller number.")
    elif guess < secret_number:
        print("Enter a larger number.")
    
    guess = int(input("Enter your guess: "))
    number_of_guesses += 1

print("Number of guesses:", number_of_guesses)
```


# Task 14.10

Write program code to implement the pseudocode from Worked Example 12.11 in Chapter 12.

```
REPEAT
 CALL OutputSpaces
 CALL OutputSymbols
 CALL AdjustValuesForNextRow
UNTIL NumberOfSymbols > MaxNumberOfSymbols

PROCEDURE SetValues
 INPUT Symbol
 CALL InputMaxNumberOfSymbols // need to ensure it is an odd number
 NumberOfSpaces ← (MaxNumberOfSymbols - 1) / 2
 NumberOfSymbols ← 1
ENDPROCEDURE
PROCEDURE InputMaxNumberOfSymbols
 REPEAT
 INPUT MaxNumberOfSymbols
 UNTIL MaxNumberOfSymbols MOD 2 = 1
ENDPROCEDURE
PROCEDURE OutputSpaces
 FOR Count1 ← 1 TO NumberOfSpaces
 OUTPUT Space // without moving to next line
 NEXT Count1
ENDPROCEDURE
PROCEDURE OutputSymbols
 FOR Count2 ← 1 TO NumberOfSymbols
 OUTPUT Symbol // without moving to next line
 NEXT Count2
 OUTPUT Newline // move to the next line
ENDPROCEDURE
PROCEDURE AdjustValuesForNextRow
 NumberOfSpaces ← NumberOfSpaces – 1
 NumberOfSymbols ← NumberOfSymbols + 2
ENDPROCEDURE
```


```python
def set_values():
    global symbol, max_number_of_symbols, number_of_spaces, number_of_symbols
    symbol = input("Enter a symbol: ")
    input_max_number_of_symbols()
    number_of_spaces = (max_number_of_symbols - 1) // 2
    number_of_symbols = 1

def input_max_number_of_symbols():
    global max_number_of_symbols
    max_number_of_symbols = int(input("Enter the maximum number of symbols (must be odd): "))
    while max_number_of_symbols % 2 == 0:
        max_number_of_symbols = int(input("Invalid input. Enter an odd number for the maximum number of symbols: "))

def output_spaces():
    for count1 in range(number_of_spaces):
        print(" ", end="")
    print(end="")

def output_symbols():
    for count2 in range(number_of_symbols):
        print(symbol, end="")
    print()

def adjust_values_for_next_row():
    global number_of_spaces, number_of_symbols
    number_of_spaces -= 1
    number_of_symbols += 2

def generate_pattern():
    set_values()
    while number_of_symbols <= max_number_of_symbols:
        output_spaces()
        output_symbols()
        adjust_values_for_next_row()

generate_pattern()
```

# Task 14.11

Write program code to implement the pseudocode from Worked Example 13.05 in Chapter 13. Which variables are global and which are local?

```
01 CALL InitialiseBoard
02 CALL SetUpGame
03 CALL OutputBoard
04 WHILE GameFinished = FALSE DO
05 CALL PlayerMakesMove
06 CALL OutputBoard
07 CALL CheckGameFinished
08 IF GameFinished = FALSE
09 THEN
10 CALL SwapThisPlayer
11 ENDIF
12 ENDWHILE

PROCEDURE InitialiseBoard
 FOR Row ← 1 TO 6
 FOR Column ← 1 TO 7
 Board[Row, Column] ← BLANK // use a suitable value for blank
 NEXT Column
 NEXT Row
ENDPROCEDURE

PROCEDURE SetUpGame
 ThisPlayer ← 'O' // Player O always starts
 GameFinished ← FALSE
ENDPROCEDURE

PROCEDURE OutputBoard
 FOR Row ← 6 DOWNTO 1
 FOR Column ← 1 TO 7
 OUTPUT Board[Row, Column] // don't move to next line
 NEXT Column
 OUTPUT Newline // move to next line
 NEXT Row
ENDPROCEDURE

PROCEDURE PlayerMakesMove
 ValidColumn ← PlayerChoosesColumn // a module returns column number
 ValidRow ← FindFreeRow // a module returns row number
 Board[ValidRow, ValidColumn] ← ThisPlayer
ENDPROCEDURE

FUNCTION PlayerChoosesColumn RETURNS INTEGER// returns a valid column number
 OUTPUT "Player ", ThisPlayer, "'s turn."
 REPEAT
 OUTPUT "Enter a valid column number: "
 INPUT ColumnNumber
 UNTIL ColumnNumberValid = TRUE // check whether the column number is valid
 RETURN ColumnNumber
ENDFUNCTION


FUNCTION ColumnNumberValid RETURNS BOOLEAN
 // returns whether or not the column number is valid
 Valid ← FALSE
 IF ColumnNumber >= 1 AND ColumnNumber <= 7
 THEN
 IF Board[6, ColumnNumber] = BLANK // at least 1 empty space in column
 THEN
 Valid ← TRUE
 ENDIF
 ENDIF
 RETURN Valid
ENDFUNCTION

FUNCTION FindFreeRow RETURNS INTEGER
 // returns the next free position
 ThisRow ← 1
 WHILE Board[ThisRow, ValidColumn] <> BLANK DO // find first empty cell
 ThisRow ← ThisRow + 1
 ENDWHILE
 RETURN ThisRow
ENDFUNCTION

PROCEDURE CheckGameFinished
 WinnerFound ← FALSE
 CALL CheckIfPlayerHasWon
 IF WinnerFound = TRUE
 THEN
 GameFinished ← TRUE
 OUTPUT ThisPlayer " is the winner"
 ELSE
 CALL CheckForFullBoard
 ENDIF
ENDPROCEDURE

PROCEDURE CheckIfPlayerHasWon
 WinnerFound ← False
 CALL CheckHorizontalLine
 IF WinnerFound = FALSE
 THEN
 CALL CheckVerticalLine
ENDPROCEDURE
PROCEDURE CheckHorizontalLine
 FOR i ← 1 TO 4
 IF Board[ValidRow, i] = ThisPlayer AND
 Board[ValidRow, i + 1] = ThisPlayer AND
 Board[ValidRow, i + 2] = ThisPlayer AND
 Board[ValidRow, i + 3] = ThisPlayer
 THEN
 WinnerFound ← TRUE
 ENDIF
 NEXT i
ENDPROCEDURE
PROCEDURE CheckVerticalLine
 IF ValidRow = 4 OR ValidRow = 5 OR ValidRow = 6
 THEN
 IF Board[ValidRow, ValidColumn] = ThisPlayer AND
 Board[ValidRow – 1, ValidColumn] = ThisPlayer AND
 Board[ValidRow – 2, ValidColumn] = ThisPlayer AND
 Board[ValidRow – 3, ValidColumn] = ThisPlayer
 THEN
 WinnerFound ← TRUE
 ENDIF
 ENDIF
ENDPROCEDURE

PROCEDURE CheckForFullBoard
 BlankFound ← FALSE
 ThisRow ← 0
 REPEAT
 ThisColumn ← 0
 ThisRow ← ThisRow + 1
 REPEAT
  ThisColumn ← ThisColumn + 1
 IF Board[ThisRow, ThisColumn] = BLANK
 THEN
 BlankFound ← TRUE
 ENDIF
 UNTIL ThisColumn = 7 OR BlankFound = TRUE
 UNTIL ThisRow = 6 OR BlankFound = TRUE
 IF BlankFound = FALSE
 THEN
 OUTPUT "It is a draw"
 GameFinished ← TRUE
 ENDIF
ENDPROCEDURE

PROCEDURE SwapThisPlayer
 IF ThisPlayer = 'O'
 THEN
 ThisPlayer ← 'X'
 ELSE
 ThisPlayer ← 'O'
 ENDIF
ENDPROCEDURE
```


```python
def initialise_board():
    global board
    board = [['BLANK' for _ in range(7)] for _ in range(6)]

def set_up_game():
    global this_player, game_finished
    this_player = 'O'
    game_finished = False

def output_board():
    for row in reversed(board):
        for cell in row:
            print(cell, end=" ")
        print()

def player_makes_move():
    valid_column = player_chooses_column()
    valid_row = find_free_row(valid_column)
    board[valid_row][valid_column] = this_player

def player_chooses_column():
    print("Player", this_player, "'s turn.")
    while True:
        column_number = int(input("Enter a valid column number: "))
        if column_number_valid(column_number):
            return column_number
        else:
            print("Invalid column number. Please enter a valid column number.")

def column_number_valid(column_number):
    if column_number >= 1 and column_number <= 7:
        if board[5][column_number-1] == 'BLANK':
            return True
    return False

def find_free_row(column_number):
    this_row = 0
    while board[this_row][column_number-1] != 'BLANK':
        this_row += 1
    return this_row

def check_game_finished():
    winner_found = check_if_player_has_won()
    if winner_found:
        print(this_player, "is the winner.")
        global game_finished
        game_finished = True
    else:
        check_for_full_board()

def check_if_player_has_won():
    winner_found = False
    check_horizontal_line()
    if not winner_found:
        check_vertical_line()
    return winner_found

def check_horizontal_line():
    for row in board:
        for i in range(4):
            if row[i] == row[i+1] == row[i+2] == row[i+3] == this_player:
                global winner_found
                winner_found = True
                return

def check_vertical_line():
    if valid_row >= 3:
        if board[valid_row][valid_column-1] == board[valid_row-1][valid_column-1] == board[valid_row-2][valid_column-1] == board[valid_row-3][valid_column-1] == this_player:
            global winner_found
            winner_found = True

def check_for_full_board():
    blank_found = False
    for row in board:
        if 'BLANK' in row:
            blank_found = True
            break
    if not blank_found:
        print("It is a draw.")
        global game_finished
        game_finished = True

def swap_this_player():
    global this_player
    if this_player == 'O':
        this_player = 'X'
    else:
        this_player = 'O'

def play_game():
    initialise_board()
    set_up_game()
    output_board()
    while not game_finished:
        player_makes_move()
        output_board()
        check_game_finished()
        if not game_finished:
            swap_this_player()

play_game()
```

- In the provided code, the variables `board`, `this_player`, `game_finished`, and `winner_found` are declared as global variables. They are defined outside of any specific function and can be accessed and modified by multiple functions.

- On the other hand, variables such as `row`, `column`, `valid_column`, `valid_row`, `column_number`, `this_row`, `this_column`, and `blank_found` are local variables. They are declared within specific functions and are only accessible within their respective functions. These variables are used for temporary storage or calculations within the scope of their corresponding functions.

- The `initialise_board` function initializes the board with the value 'BLANK' for each cell.

- The `set_up_game` function sets the initial player to 'O' and the game_finished flag to False.

- The `output_board` function prints the board, iterating over each row and column.

- The `player_makes_move` function prompts the player to choose a column, finds the valid row to place the player's move, and updates the board.

- The `player_chooses_column` function asks the player to input a valid column number, repeatedly prompting until a valid number is entered.

- The `column_number_valid` function checks if the entered column number is valid based on the conditions provided.

- The `find_free_row` function finds the next available row in the given column.

- The `check_game_finished` function checks if the game is finished by calling `check_if_player_has_won` and `check_for_full_board`.

- The `check_if_player_has_won` function checks if the current player has won the game by calling `check_horizontal_line` and `check_vertical_line`.

- The `check_horizontal_line` function checks for a horizontal line of four matching symbols in a row.

- The `check_vertical_line` function checks for a vertical line of four matching symbols in a column.

- The `check_for_full_board` function checks if the board is full and declares a draw if no more moves can be made.

- The `swap_this_player` function swaps the current player between 'O' and 'X'.

- The `play_game` function encompasses the main game logic, initializing the board, setting up the game, outputting the board, and iterating over player moves until the game is finished.

# Task 14.12

Write a function to implement the following pseudocode:
```
FUNCTION Factorial (Number : INTEGER) RETURNS INTEGER
 DECLARE Product : INTEGER
 Product ← 1
 FOR n ← 2 TO Number
 Product ← Product * n
 NEXT n
 RETURN Product
ENDFUNCTION
```

```python
def factorial(number):
    product = 1
    for n in range(2, number+1):
        product *= n
    return product
```


# Task 14.13

1. Write program code to implement the pseudocode from Worked Example 13.01 in Chapter 13.
2. Write program code to implement the pseudocode from Worked Example 13.02 in Chapter 13.
3. Write program code to implement the improved algorithm from Worked Example 13.03 in Chapter 13.

## Answers

1.
```
FOR Index ← 0 TO 6
 INPUT MyList[Index]
NEXT Index
```

```
MyList = []
for Index in range(7):
    MyList.append(input())
```

2.

```
MaxIndex ← 6
INPUT SearchValue
Found ← FALSE
Index ← –1
REPEAT
 Index ← Index + 1
 IF MyList[Index] = SearchValue
 THEN
 Found ← TRUE
 ENDIF
UNTIL FOUND = TRUE OR Index >= MaxIndex
IF Found = TRUE
 THEN
 OUTPUT "Value found at location: " Index
 ELSE
 OUTPUT "Value not found"
ENDIF
```

```python
MaxIndex = 6
SearchValue = input("Enter the search value: ")
Found = False
Index = -1

while not Found and Index < MaxIndex:
    Index = Index + 1
    if MyList[Index] == SearchValue:
        Found = True

if Found:
    print("Value found at location:", Index)
else:
    print("Value not found")
```

3. 

```
n ← MaxIndex – 1
REPEAT
 NoMoreSwaps ← TRUE
 FOR j ← 0 TO n
 IF MyList[j] > MyList[j + 1]
THEN
 Temp ← MyList[j]
 MyList[j] ← MyList[j + 1]
 MyList[j + 1] ← Temp
 NoMoreSwaps ← FALSE
 ENDIF
 NEXT j
 n ← n – 1
UNTIL NoMoreSwaps = TRUE
```

```python
n = MaxIndex - 1
NoMoreSwaps = False

while not NoMoreSwaps:
    NoMoreSwaps = True
    for j in range(n):
        if MyList[j] > MyList[j + 1]:
            Temp = MyList[j]
            MyList[j] = MyList[j + 1]
            MyList[j + 1] = Temp
            NoMoreSwaps = False
    n = n - 1
```

```python
def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n - 1):
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Example usage:
array = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(array)
print("Sorted array:", array)
```


# Task 14.14
1. Write program code to implement the pseudocode from Worked Example 13.04 in Chapter 13; first initialise the table and then output its contents.
2. Write program code to implement the pseudocode from Worked Example 13.05 in Chapter 13.

## Asnwers

1. 

```

FOR Row ← 0 TO MaxRowIndex
 FOR Column ← 0 TO MaxColumnIndex
 OUTPUT ThisTable[Row, Column] // stay on same line
 NEXT Column
 OUTPUT Newline // move to next line for next row
NEXT Row
```

```python
for Row in range(MaxRowIndex + 1):
    for Column in range(MaxColumnIndex + 1):
        print(ThisTable[Row][Column], end=" ")
    print()  # Prints a newline to move to the next line for the next row
```

2.
```
The top-level pseudocode version using modules is:
01 CALL InitialiseBoard
02 CALL SetUpGame
03 CALL OutputBoard
04 WHILE GameFinished = FALSE DO
05 CALL PlayerMakesMove
06 CALL OutputBoard
07 CALL CheckGameFinished
08 IF GameFinished = FALSE
09 THEN
10 CALL SwapThisPlayer
11 ENDIF
12 ENDWHILE

PROCEDURE InitialiseBoard
 FOR Row ← 1 TO 6
 FOR Column ← 1 TO 7
 Board[Row, Column] ← BLANK // use a suitable value for blank
 NEXT Column
 NEXT Row
ENDPROCEDURE

PROCEDURE SetUpGame
 ThisPlayer ← 'O' // Player O always starts
 GameFinished ← FALSE
ENDPROCEDURE
PROCEDURE OutputBoard
 FOR Row ← 6 DOWNTO 1
 FOR Column ← 1 TO 7
 OUTPUT Board[Row, Column] // don't move to next line
 NEXT Column
 OUTPUT Newline // move to next line
 NEXT Row
ENDPROCEDURE
PROCEDURE PlayerMakesMove
 ValidColumn ← PlayerChoosesColumn // a module returns column number
 ValidRow ← FindFreeRow // a module returns row number
 Board[ValidRow, ValidColumn] ← ThisPlayer
ENDPROCEDURE

FUNCTION PlayerChoosesColumn RETURNS INTEGER// returns a valid column number
 OUTPUT "Player ", ThisPlayer, "'s turn."
 REPEAT
 OUTPUT "Enter a valid column number: "
 INPUT ColumnNumber
 UNTIL ColumnNumberValid = TRUE // check whether the column number is valid
 RETURN ColumnNumber
ENDFUNCTION

FUNCTION ColumnNumberValid RETURNS BOOLEAN
 // returns whether or not the column number is valid
 Valid ← FALSE
 IF ColumnNumber >= 1 AND ColumnNumber <= 7
 THEN
 IF Board[6, ColumnNumber] = BLANK // at least 1 empty space in column
 THEN
 Valid ← TRUE
 ENDIF
 ENDIF
 RETURN Valid
ENDFUNCTION

FUNCTION FindFreeRow RETURNS INTEGER
 // returns the next free position
 ThisRow ← 1
 WHILE Board[ThisRow, ValidColumn] <> BLANK DO // find first empty cell
 ThisRow ← ThisRow + 1
 ENDWHILE
 RETURN ThisRow
ENDFUNCTION

PROCEDURE CheckGameFinished
 WinnerFound ← FALSE
 CALL CheckIfPlayerHasWon
 IF WinnerFound = TRUE
 THEN
 GameFinished ← TRUE
 OUTPUT ThisPlayer " is the winner"
 ELSE
 CALL CheckForFullBoard
 ENDIF
ENDPROCEDURE

PROCEDURE CheckIfPlayerHasWon
 WinnerFound ← False
 CALL CheckHorizontalLine
 IF WinnerFound = FALSE
 THEN
 CALL CheckVerticalLine
ENDPROCEDURE
PROCEDURE CheckHorizontalLine
 FOR i ← 1 TO 4
 IF Board[ValidRow, i] = ThisPlayer AND
 Board[ValidRow, i + 1] = ThisPlayer AND
 Board[ValidRow, i + 2] = ThisPlayer AND
 Board[ValidRow, i + 3] = ThisPlayer
 THEN
 WinnerFound ← TRUE
 ENDIF
 NEXT i
ENDPROCEDURE
PROCEDURE CheckVerticalLine
 IF ValidRow = 4 OR ValidRow = 5 OR ValidRow = 6
 THEN
 IF Board[ValidRow, ValidColumn] = ThisPlayer AND
 Board[ValidRow – 1, ValidColumn] = ThisPlayer AND
 Board[ValidRow – 2, ValidColumn] = ThisPlayer AND
 Board[ValidRow – 3, ValidColumn] = ThisPlayer
 THEN
 WinnerFound ← TRUE
 ENDIF
 ENDIF
ENDPROCEDURE
PROCEDURE CheckForFullBoard
 BlankFound ← FALSE
 ThisRow ← 0
 REPEAT
 ThisColumn ← 0
 ThisRow ← ThisRow + 1
 REPEAT
ThisColumn ← ThisColumn + 1
 IF Board[ThisRow, ThisColumn] = BLANK
 THEN
 BlankFound ← TRUE
 ENDIF
 UNTIL ThisColumn = 7 OR BlankFound = TRUE
 UNTIL ThisRow = 6 OR BlankFound = TRUE
 IF BlankFound = FALSE
 THEN
 OUTPUT "It is a draw"
 GameFinished ← TRUE
 ENDIF
ENDPROCEDURE

PROCEDURE SwapThisPlayer
 IF ThisPlayer = 'O'
 THEN
 ThisPlayer ← 'X'
 ELSE
 ThisPlayer ← 'O'
 ENDIF
ENDPROCEDURE

Initialise board
Set up game
Display board
While game not finished
 Player makes a move
 Display board
 Check if game finished
 If game not finished, swap player
 ```
 
 ```python
 def initialise_board():
    for row in range(1, 7 + 1):
        for column in range(1, 7 + 1):
            Board[row][column] = BLANK  # Use a suitable value for BLANK

def set_up_game():
    global ThisPlayer, GameFinished
    ThisPlayer = 'O'  # Player O always starts
    GameFinished = False

def output_board():
    for row in range(6, 0, -1):
        for column in range(1, 7 + 1):
            print(Board[row][column], end=" ")
        print()  # Prints a newline to move to the next line

def player_makes_move():
    ValidColumn = player_chooses_column()  # A module that returns a valid column number
    ValidRow = find_free_row()  # A module that returns a valid row number
    Board[ValidRow][ValidColumn] = ThisPlayer

def player_chooses_column():
    print("Player", ThisPlayer, "'s turn.")
    while True:
        ColumnNumber = int(input("Enter a valid column number: "))
        if column_number_valid(ColumnNumber):
            return ColumnNumber

def column_number_valid(ColumnNumber):
    if 1 <= ColumnNumber <= 7:
        if Board[6][ColumnNumber] == BLANK:  # At least 1 empty space in column
            return True
    return False

def find_free_row():
    ThisRow = 1
    while Board[ThisRow][ValidColumn] != BLANK:  # Find the first empty cell
        ThisRow += 1
    return ThisRow

def check_game_finished():
    global GameFinished
    winner_found = check_if_player_has_won()
    if winner_found:
        GameFinished = True
        print(ThisPlayer, "is the winner")
    else:
        check_for_full_board()

def check_if_player_has_won():
    winner_found = False
    check_horizontal_line()
    if not winner_found:
        check_vertical_line()
    return winner_found

def check_horizontal_line():
    for i in range(1, 4 + 1):
        if (
            Board[ValidRow][i] == ThisPlayer and
            Board[ValidRow][i + 1] == ThisPlayer and
            Board[ValidRow][i + 2] == ThisPlayer and
            Board[ValidRow][i + 3] == ThisPlayer
        ):
            winner_found = True

def check_vertical_line():
    if ValidRow >= 4 and ValidRow <= 6:
        if (
            Board[ValidRow][ValidColumn] == ThisPlayer and
            Board[ValidRow - 1][ValidColumn] == ThisPlayer and
            Board[ValidRow - 2][ValidColumn] == ThisPlayer and
            Board[ValidRow - 3][ValidColumn] == ThisPlayer
        ):
            winner_found = True

def check_for_full_board():
    blank_found = False
    for ThisRow in range(1, 6 + 1):
        for ThisColumn in range(1, 7 + 1):
            if Board[ThisRow][ThisColumn] == BLANK:
                blank_found = True
                break
        if blank_found:
            break
    if not blank_found:
        print("It is a draw")
        GameFinished = True

def swap_this_player():
    global ThisPlayer
    if ThisPlayer == 'O':
        ThisPlayer = 'X'
    else:
        ThisPlayer = 'O'


# Main program
Board = [[None] * 8 for _ in range(7)]  # Assuming the board is 7x7
BLANK = ' '

initialise_board()
set_up_game()
output_board()

while not GameFinished:
    player_makes_move()
    output_board()
    check_game_finished()
    if not GameFinished:
        swap_this_player()
```


# Task 14.15

Fred surveys the students at his college to find out their favourite hobby. 
- He wants to present the data as a tally chart.
- Fred plans to enter the data into the computer as he surveys the students. After data entry is complete, he wants to output the total for each hobby. 

```
1 Reading books 			 \\\
2 Play computer games  \\\\\\\\
3 Sport 							  \\\\\
4 Programming 					 \\
5 Watching TV 					 \\\\\\\\\\\
```

He starts by writing an algorithm:

```
Initialise Tally array
REPEAT
 INPUT Choice // 1 for Reading, 2 for computer games,
// 3 for Sport, 4 for Programming, 5 for TV
// 0 to end input
 Increment Tally[Choice]
UNTIL Choice = 0
FOR Index = 1 TO 5
 OUTPUT Tally[Index]
NEXT Index
```

1. Write program code to declare and initialise the array Tally : ARRAY[1:5] OF INTEGER.
2. Write program code to implement the algorithm above.
3. Write program code to declare an array to store the hobby titles and rewrite the FOR loop of your program in part 2 so that the hobby title is output before each tally.
4. Write program code to save the array data in a text file.
5. Write program code to read the data from the text file back into the initialised array

## Answers

1. 

```python
Tally = [0] * 5
```

2. 

```python
Tally = [0] * 5

while True:
    choice = int(input("Enter the hobby choice (1-5) or 0 to end input: "))
    if choice == 0:
        break
    Tally[choice - 1] += 1

for index in range(5):
    print(Tally[index])
```

3. 

```python
Tally = [0] * 5
Hobbies = ["Reading books", "Play computer games", "Sport", "Programming", "Watching TV"]

while True:
    choice = int(input("Enter the hobby choice (1-5) or 0 to end input: "))
    if choice == 0:
        break
    Tally[choice - 1] += 1

for index in range(5):
    print(Hobbies[index] + ": " + str(Tally[index]))
```

4. 

```python
Tally = [0] * 5
Hobbies = ["Reading books", "Play computer games", "Sport", "Programming", "Watching TV"]

while True:
    choice = int(input("Enter the hobby choice (1-5) or 0 to end input: "))
    if choice == 0:
        break
    Tally[choice - 1] += 1

with open("hobby_data.txt", "w") as file:
    for index in range(5):
        file.write(Hobbies[index] + ": " + str(Tally[index]) + "\n")

print("Data saved to hobby_data.txt file.")
```

5. 

```python
Tally = [0] * 5
Hobbies = ["Reading books", "Play computer games", "Sport", "Programming", "Watching TV"]

with open("hobby_data.txt", "r") as file:
    lines = file.readlines()
    for index, line in enumerate(lines):
        tally = line.strip().split(": ")[1]
        Tally[index] = int(tally)

for index in range(5):
    print(Hobbies[index] + ": " + str(Tally[index]))
```



