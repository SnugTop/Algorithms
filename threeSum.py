def find_three_sum(A, n, x):
    copyOfA = A[:]
    A.sort()
    Left = 0
    
    while Left < n - 2:
        m = Left + 1
        Right = n - 1
        
        while m < Right:
            Sum = A[Left] + A[m] + A[Right]
            
            if Sum == x:
                Val1 = A[Left]
                Val2 = A[m]
                Val3 = A[Right]
                
                Index1 = copyOfA.index(Val1) + 1
                Index2 = copyOfA.index(Val2) + 1
                Index3 = copyOfA.index(Val3) + 1
                
                if Index1 == Index2:
                    Index2 = copyOfA.index(Val2, Index1) + 1
                
                if Index1 == Index3:
                    Index3 = copyOfA.index(Val3, Index1) + 1
                
                if Index2 == Index3:
                    Index3 = copyOfA.index(Val3, Index2) + 1
                
                return Index1, Index2, Index3

            elif Sum < x:
                m += 1
            
            else:
                Right -= 1
        
        Left += 1
    
    return -1

A = [8, 7, 8, 9, 15]
n = len(A)
x = 24

result = find_three_sum(A, n, x)
print(result)
