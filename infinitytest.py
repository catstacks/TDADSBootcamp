# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6

    # find sum of Ns digits 
    

    total = 0

    for i in str(N):
        total = total + int(i)
        
    
   


    double = total * 2

       
    for a in range(N + 1, 500):
        new_total = 0

        for i in str(a):
            new_total = new_total + int(i)
            
            if new_total == double:
                print(type(a))
                return int(a)
           

solution(14)
solution(99)               

def solution(A):
    # write your code in Python 3.6

    # 
    if len(A) % 2 != 0:
        return False
    
    
    
    for i in A:
        if (2 * i) % 2 != 0:
            return False
        else:
            return True

# for i in A:
    
#     return True
#     return False        
