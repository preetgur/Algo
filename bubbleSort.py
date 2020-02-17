"""
# It is the technique of sorting array in ascending order

# Notice that after each iteration, at least one value moves at the end.[The greater value]
# That's why we are using the len(li)-1 : not refer to the last index's which is sorted.

# important tip : when we have to sorted from backside use len(li)-1 upto 0 with decreaseing of -1
range(len(li)-1,0,-1)   => range(starting index, last index ,increment)


"""
def bubble_sort(li):

    increment = 0
    for i in range(len(li)-1,0,-1):   # This loop is used for iteration
        increment = increment+1
        for j in range(i):
            # If first index value is greater than second index value
            if li[j] > li[j + 1]:

                #swap values
                li[j],li[j+1] = li[j+1],li[j]

        print(f" {increment} Iteration : {li}")


li = [12,1,78,34,7,8,99,5,6]

bubble_sort(li)
