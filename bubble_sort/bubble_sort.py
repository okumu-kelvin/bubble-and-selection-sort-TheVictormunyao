def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort
    pass
#To iterate through the list
    for n in range(len(unsorted_list)-1, 0, -1):
        #Inner loop to compare adjacent elements
        
        for i in range(n):
            if unsorted_list[i]>unsorted_list[i+1]:
                #Swap the elements if they are in the wrong order
                unsorted_list[i],unsorted_list[i+1]=unsorted_list[i+1],unsorted_list[i]
    return unsorted_list           
      
      



unsorted_list =[32,43,20,76,65,19]
print("Unsorted list : ", unsorted_list)

print("sorted list : ", bubble_sort(unsorted_list))
