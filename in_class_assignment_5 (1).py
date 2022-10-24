# Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.


'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British computer scientist Tony Hoare in 1959.

Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to sort. You start by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists based on the pivot item and recursively sort the sublists.

The steps of the algorithm are as follows:

1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 

The base cases occur when the sublists are either empty or have one element, as these are inherently sorted. 
 '''


def swapElements(numbers_in_a_list, ind1, ind2):
    tempElement = numbers_in_a_list[ind1]
    numbers_in_a_list[ind1] = numbers_in_a_list[ind2]
    numbers_in_a_list[ind2] = tempElement


# function to perform quicksort
def quickSort(numbers_in_a_list, p, r):
    if p <= r - 1:
        pivPointer = numbers_in_a_list[r]
        i = p - 1
        for j in range(p, r):
            if numbers_in_a_list[j] < pivPointer + 1:
                i = i + 1
                swapElements(numbers_in_a_list, i, j)

        swapElements(numbers_in_a_list, i + 1, r)
        q = i + 1
        quickSort(numbers_in_a_list, p, q - 1)
        quickSort(numbers_in_a_list, q + 1, r)


def main():
    # WRITE YOUR MAIN FUNCTION HERE TO READ IN YOUR numbers.txt FILE, RUN THE LIST THROUGH YOUR SORTING ALGORITHM,
    # AND WRITE OUT YOUR FILE

    file = open("numbers.txt", "r+")

    x = file.readlines()
    y = str(x)[3:len(str(x)) - 3]
    string = y.split(', ')

    res = []
    for i in string:
        res.append(int(i))

    quickSort(res, 0, len(res) - 1)

    with open('sorted.txt', 'w') as f:
        f.write(str(res))

    return 0


if __name__ == "__main__":
    main()
