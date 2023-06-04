# TASK 13.05

Rewrite the algorithm in Worked Example 13.03 to sort the array elements into
descending order.

### Descending Order

```
n ← MaxIndex – 1
REPEAT
    NoMoreSwaps ← TRUE
    FOR j ← 0 TO n
        IF MyList[j] < MyList[j + 1]      // <--- this is changed
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

### Ascending Order

```
n ← MaxIndex – 1
REPEAT
    NoMoreSwaps ← TRUE
    FOR j ← 0 TO n
        IF MyList[j] > MyList[j + 1]    // <--- this is changed
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

# Difference
