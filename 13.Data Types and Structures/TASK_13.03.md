# TASK 13.03

Define two arrays, one for your friends’ names and one for their ages as shown in
Figure 13.02

```
DECLARE friendNames: ARRAY[0:19] OF STRING
DECLARE friendAges: ARRAY[0:19] OF INTEGER

FOR i <- 0 to 19
    OUTPUT "Name: "
    INPUT friendNames[i]
    OUTPUT "Age: "
    INPUT friendAges[i]
NEXT i
```
