####### Linear Search Using While Loop

def linearSearch(li,n):

    i = 0
    while i < len(li):
        if li[i] == n:
            return True
        i = i+1 
    return False


li= [1,3,5,6,7,3]
n = 5

if  linearSearch(li,n):
    print(f"Found {n} : At  index ")
else :
    print("!!! Not Found")


############ Linear Search Using For Loop and using some global variables

index_pos = 0          # simple variable\
msg = ""
def for_loop_linear(li,n):
    for i in range(len(li)) :
        if li[i] == n:
            globals() ['index_pos'] = i      # making global varible :=> globals()[''] and assign value
            globals() ['msg'] = "some Kind of message"
            return True,msg
    return False

n = 6
if  for_loop_linear(li,n):
    print(f"Found {n} : At {index_pos} index [for-loop] , {msg} ")
else :
    print("!!! Not Found {n} : [for-loop] ")


