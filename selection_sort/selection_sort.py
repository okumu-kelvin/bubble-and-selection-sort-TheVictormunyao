def selection_sort(arr):
    # TODO: Implement selection sort
    for i in range(len(arr)):
        min_element = i
        for j in range(i + 1, len(arr)):
            # selecting the minimum element in each iteration
            if arr[j] < arr[min_element]:
                min_element = j
        # swapping the elements to sort the array         
        arr[i], arr[min_element] = arr[min_element], arr[i]
    return arr

# Array to be sorted
arr = [9,3,5,78,72,2,1]
print("Unsorted list : ",arr)

print ("Sorted list", selection_sort(arr))
