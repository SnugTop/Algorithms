def find_sum(A, n, x):
    original_A = A[:]
    A.sort()
    
    Left = 0
    Right = n - 1
    
    while Left < Right:
        Sum = A[Left] + A[Right]
        
        if Sum == x:
            value1 = A[Left]
            value2 = A[Right]
            
            index1 = original_A.index(value1) + 1
            index2 = original_A.index(value2) + 1
            
            if index1 == index2:
                index2 = original_A.index(value2, index1)
            
            return index1, index2
        
        elif Sum < x:
            Left += 1
        
        else:
            Right -= 1
    
    return -1

A = [8, 7, 8, 9, 15]
n = len(A)
x = 16

result = find_sum(A, n, x)
print(result)
