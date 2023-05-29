"""
Bubble Sort - Basic Sorting Algorithm

How does it work?
    https://www.youtube.com/watch?v=Jdtq5uKz-w4

Pseudocode:
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

Summary:
    Bubble sort is a simple comparison-based sorting 
    algorithm. It works by repeatedly swapping adjacent 
    elements if they are in the wrong order until the 
    entire list is sorted. Here's a summary of how the 
    bubble sort algorithm works:

    1. Start with an unsorted list of elements.
    2. Compare the first element with the second 
    element.
    3. If the first element is greater than the second 
    element, swap them.
    4. Move to the next pair of adjacent elements and repeat 
    the comparison and swapping process.
    5. Continue this process until you reach the end of the 
    list. At this point, the largest element will be in 
    its correct position at the end of the list.
    6. Repeat steps 2-5 for the remaining unsorted portion 
    of the list (excluding the last sorted element).
    7. Keep repeating steps 2-6 until the entire list is 
    sorted.

    The key idea behind bubble sort is that with each pass, 
    the largest unsorted element "bubbles" to its correct 
    position at the end of the list. By repeatedly going 
    through the list and comparing adjacent elements, 
    bubble sort gradually sorts the elements from the 
    beginning to the end.
"""

def while_for_implentation(list_a):
    indexing_length = len(list_a) - 1 #SCan not apply comparision starting with last item of list (No item to right)
    sorted = False #Create variable of sorted and set it equal to false

    while not sorted:  #Repeat until sorted = True
        sorted = True  # Break the while loop whenever we have gone through all the values

        for i in range(0, indexing_length): # For every value in the list
            if list_a[i]: #"Angled brackets not allowed in Youtube Description :( list_a[i+1]: #if value in list is greater than value directly to the right of it,
                sorted = False # These values are unsorted
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i] #Switch these values
    return list_a # Return our list "unsorted_list" which is not sorted.

def for_for_1_implentation(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def for_for_2_implentation(arr):
    n = len(arr)
    
    # Traverse through all array elements in reverse order
    for i in range(n - 1, 0, -1):
        
        # Iterate from the beginning to the current position
        for j in range(i):
            
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


