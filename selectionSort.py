# Selection sort
"""
Divides the list into two parts, Sorted part to the "left" end and unsorted part to the "right" end.
Initially sorted part is empty and unsorted part in the entire list.

Procedures:
The smallest element is selected from  the unsorted array and swapped with the leftmost element, and
that element becomes a part or the sorted array.

"""

def selectionSort(li):

    for i in range(len(li)):
        min_pos = i     # holds index value, changes according the for loop runs

        for j in range(i,len(li)):
            # we are taking first element of the list and compare with the other elements is list.
            #If other elements are less than first element "min_pos" than update its index
            if li[j] < li[min_pos]:
                min_pos = j

        # swap the values
        li[i],li[min_pos] = li[min_pos],li[i]


li = [5,69,3,8,6,7,2,65,9]
selectionSort(li)
print(li)