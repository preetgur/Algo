index_pos = -1

def binarySearch(li,n):

    lower_bound = 0
    upper_bound = len(li)-1  
    
    while lower_bound < upper_bound:
        mid = (lower_bound+upper_bound)//2    # middle index value
        print("Mid : ", mid)

        if li[mid] == n:              # Access the value with the help of mid [index value]
            globals()['index_pos'] = mid
            return True

        else:
            # value is greater than mid value            
            if li[mid] < n:
                # update lower-bound to mid

                lower_bound = mid+1               

            else:
                #update Upper-bound
                
                upper_bound = mid-1
    return False              
               
############## End of Function ###########    

li = [5,7,9,12,15,40,67,87,98,99,121,143]  # Sorted list
n = 12

print("Length : ",len(li))
if binarySearch(li,n):
    print(f"Found {n} at index {index_pos} ")
else :
    print(f"Not Found {index_pos} ")    