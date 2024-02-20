def selection_sort(A): 
    for i in range(len(A)-1): #(inner loop) interate trough the list from start to last element 
        min_index = i #set i as the first index
        for j in range(i+1, len(A)): #loop through the array
            if A[j] < A[min_index]: #If the number is lower than the min_index
                min_index = j   #Set the min_index as the number we compare
        if min_index != i: #This if is used to otimize the code
             A[i], A[min_index] = A[min_index], A[i] #function to swap them
    return A 

A = [11, 22, 14, 67, 2, 9]
print(A)
print(selection_sort(A))
