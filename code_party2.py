def sum_of_element(numbers):

    number_list = []

    for inside_list in numbers:
        sum = 0
        
        for number in inside_list:
            sum+= number
        number_list.append(sum)
    return number_list
 
numbers =  [ [2, 3, 4],  [1, 5, 7],  [4, 6, 8] ]
print(sum_of_element(numbers))



def sum_of_index(numbers):
    index_list = []
    
    for index in range(len(numbers[0])):
    
        total = 0
        for inner_list in numbers:
            total =+ inner_list[index] 
        index_list.append(total)
    return index_list
numbers =  [ [2, 3, 4],  [1, 5, 7],  [4, 6, 8] ]
print(sum_of_index(numbers))
