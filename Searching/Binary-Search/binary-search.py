

# for the binary search array is need to sorted order ascending or descending 

def binary_search(arr , target) : 
    # Iterate on array using two pointer start and end 
    start = 0 
    end = len(arr) - 1 

    while start <= end : 
        # finding the mid element 
        mid = (start + end ) // 2 
        # check that middle element == target if yes we found are ans 
        if target == arr[mid] : 
            return mid 
        # if target is > then mid element then ans on the right hand side 
        elif target > arr[mid] :
            start = mid + 1     
        
        # if target < mid element then ans is on the hand side 
        else : 
            end = mid - 1 

    # This Line is executed means we dont have element in the array to return -1 
    return -1  


arr = [11,22,44,54,71,81,91]  
target = 911

ans = binary_search(arr , target) 
print ("Ans The Index is : " , ans)

