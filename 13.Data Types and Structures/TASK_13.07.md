# TASK 13.07

1. Declare an array of BookType (see Task 13.02) for 200 books.

2. Set the first book’s details to the values given in Task 13.02.

```
TYPE BookDetails
    DECLARE title: STRING
    DECLARE year: INTEGER
    DECLARE price: REAL
    DECLARE isbn: STRING
ENDTYPE

DECLARE books: ARRAY[0:199] OF BookDetails

books[0].title <- "Computer Science"
books[0].year <- 2019
books[0].price <- 44.95
books[0].isbn <- “9781108733755”
```
