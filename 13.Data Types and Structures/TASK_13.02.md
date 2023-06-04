# TASK 13.02

Write the declaration of a record type to store the details of a book: Title, Year of
publication, Price, ISBN.
Write the statements required to assign the values “Computer Science”, 2019, £44.95,
“9781108733755” to the fields respectively

```
TYPE BookDetails
    DECLARE title: STRING
    DECLARE year: INTEGER
    DECLARE price: REAL
    DECLARE isbn: STRING
ENDTYPE

DECLARE Book1: BookDetails

Book1.title <- "Computer Science"
Book1.year <- 2019
Book1.price <- 44.95
Book1.isbn <- “9781108733755”
```
