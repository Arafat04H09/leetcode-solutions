    So the idea is that we initally set a max_so_far which is initally taken as the first ele of arr
    
    secondly we are checking two things first if max_so_far < arr[i] if so then update max_so_far
    
    and then we are checking that once the max_so_far has reached the index which is equal to it,
    
    means that that if the maximum where it can be in a sorted arr or in other words that it is 
    
    the max it can impact. So we will incremnt the count and keep going that way.
    
    THIS TECHNIQUE IS CALLED CHAIN TECHNIQUE  
     
   
    max_so_far = arr[0]
    
    count = 0
    
    for i in range(len(arr)):
        if max_so_far<arr[i]:
            max_so_far = arr[i]
            
        if max_so_far == i:
            count+=1
            
    return count
	