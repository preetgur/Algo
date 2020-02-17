# MergeSort
"""
Procedure :
First Divides the list into two half (left or right).
Then again divides the left or right half into another (left or right half).
Then process goes on untill the length of list is greater than one [ len(li)>1 ].

Now Compare the left and right half values and them merge it.
"""
def mergeSort(li):

    print("Spliting.. ",li)
    if len(li)>1:
        mid = len(li)//2
        ############ Important  : divides the list into left or right half
        left_half = li[:mid] # 0 to mid
        right_half = li[mid:]  # mid to end

        # Below fxn runs until the len(li) is eaual to 1
        mergeSort(left_half)   # split the left half  [recursively calling the function]
        # when if condition fails goes out of the loop and calling the fxn with right half
        mergeSort(right_half)  # split the right half

        # when the above if stmt fails then it comes here :
        # here it contains the  list that contains the lasts "left" and "right" halfs
        # ex.   li [54,7]
        #       left half : 54    len(left) = 1
        #       right half : 7
        """
        "i" is related to left_half index
        "j" is related to right_half index
        "k" is related to li index
        
        """
        i = j = k = 0
        # when the length of left and right halfs is greater than "i,j" values
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                li[k]=left_half[i]  # if left half  is small update the list  with that index value
                i=i+1
            else:
                # if left half is greater
                li[k]=right_half[j]
                j=j+1               # increment the index of riht half
            k=k+1                 # increment the index of list

        # when the length of left half is greter than i
        while i < len(left_half):
            li[k]=left_half[i]     # li[k] ,k = 1 updated in above while loop
            i=i+1               # increment the left half index
            k=k+1               # increment the list index

        # when the length of left right is greter than j
        while j < len(right_half):
            li[k]=right_half[j]
            j=j+1
            k=k+1

        print("merge : ",li)

li = [3,54,7,88,2,53]
mergeSort(li)
