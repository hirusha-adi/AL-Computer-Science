# TASK 13.04

Use the algorithm in Worked Example 13.02 as a design pattern. Write an algorithm
using the arrays from Task 13.03 to search for a friend’s name and output their age.

```
DECLARE friendNames: ARRAY[0:19] OF STRING
DECLARE friendAges: ARRAY[0:19] OF INTEGER


OUTPUT "Name: "
INPUT checkName

found <- TRUE
i <- -1
maxIndex <- 19

REPEAT
    i <- i + 1
    IF friendNames[i] == checkName THEN
        FOUND <- TRUE
        foundIndex <- i
    ENDIF
    INPUT friendAges[i]
UNTIL FOUND = TRUE OR i >= 19

IF found = TRUE THEN
    OUTPUT "The age is: " friendAges[foundIndex]
ELSE
    OUTPUT "Friend Name not found"
ENDIF
```
