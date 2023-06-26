# https://us04web.zoom.us/j/73913704590?pwd=bAJPGqFXFaYbgT493T0Hzka9yCsczb.1


"""

Write pseudocode for a function isDivisible() that takes two integer parameters, x and y.
The function is to return the value True or False to indicate whether x is exactly divisible by y.
For example, isDivisible(24, 6) should return True and isDivisible(24, 7) should
return False.

FUNCTION isDivisible(x, y) RETURNS BOOLEAN:
    IF x % y = 0 THEN
        RETURN True
    ELSE
        RETURN False


A poultry farm packs eggs into egg boxes. Each box takes six eggs. Boxes must not contain
fewer than six eggs.
Write pseudocode for a procedure EggsIntoBoxes that takes an integer parameter,
NumberOfEggs. The procedure is to calculate how many egg boxes can be filled with the
given number of eggs and how many eggs will be left over. The procedure is to return two
values as parameters, NumberOfBoxes and EggsLeftOver

FUNCTION EggsIntoBoxes(NumberOfEggs)
    NumberOfBoxes = NumberOfEggs / 6
    EggsLeftOver = NumberOfEggs % 6
    RETURN NumberOfBoxes, EggsLeftOver

In a certain country, car registrations consist 7 alphanumerical characters. The format of a
car reg is either
 LLNNLLL
 or
 LLLNNLL
where L is any capital letter and N is any numeral 0 to 9.
Use pseudocode to write a function that takes a string as parameter and returns TRUE if the
format is valid and FALSE otherwise.
The string-handling functions available are those listed in Table 14.06. 

"""

def type2(reg: str):
    first3c = reg[:3]
    second2c = reg[3:5]
    last2c = reg[5:]
    if not first3c.isalpha() or not first3c.isupper():
        return False
    if not second2c.isdigit():
        return False
    if not last2c.isalpha() or not last2c.isupper():
        return False
    return True

def type1(reg: str):
    first2c = reg[:2]
    second2c = reg[2:4]
    last3c = reg[4:]

    if not first2c.isalpha() or not first2c.isupper():
        return False
    if not second2c.isdigit():
        return False
    if not last3c.isalpha() or not last3c.isupper():
        return False

    return True

def isValid(reg: str) -> bool:
    if len(reg) != 7:
        return False
    first3c = reg[:3]
    if not first3c.isalpha() or not first3c.isupper():
        return type1()
    return type2()
    

# ==========================================================

def type2(reg: str):
    first3c, second2c, last2c = reg[:3], reg[3:5], reg[5:]
    if (not(first3c.isalpha()) or not(first3c.isupper())) \
        or (not second2c.isdigit()) or (not last2c.isalpha() or not last2c.isupper()):
        return False
    return True

def type1(reg: str):
    first2c, second2c, last3c = reg[:2], reg[2:4], reg[4:]
    if (not first2c.isalpha() or not first2c.isupper()) \
        or (not second2c.isdigit()) or (not last3c.isalpha() or not last3c.isupper()):
        return False
    return True

def isValid(reg: str) -> bool:
    if len(reg) != 7:
        return False
    first3c = reg[:3]
    if not first3c.isalpha() or not first3c.isupper():
        return type1(reg)
    return type2(reg)


"""

FUNCTION isValid(reg):
    if length(reg) is not equal to 7:
        RETURN False

    first3c = substring(reg, 0, 2)
    second2c = substring(reg, 2, 4)
    last2c = substring(reg, 5, 7)

    IF isUpperCase(first3c) = False THEN
        RETURN False

    IF isDigit(second2c) is False:
        RETURN False

    IF isUpperCase(last2c) is False:
        RETURN False

    IF (isUpperCase(reg[0]) and isUpperCase(reg[1]) and isDigit(reg[2]) and 
        isDigit(reg[3]) and isDigit(reg[4]) and isUpperCase(reg[5]) and 
        isUpperCase(reg[6])):
        RETURN True
    ELSE
        RETURN False

        
"""




