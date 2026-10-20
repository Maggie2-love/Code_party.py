numbers = range(1,51)
from functools import reduce

def sum_of_number(total,value):
    return total+ value

total =reduce(sum_of_number, numbers)
print(total)



numbers = [3, 5, 9, 2, 8]
from functools import reduce

def maximum_number(max, value):
    return max if max > value else value
result =reduce(maximum_number, numbers)

print(result)


from functools import reduce
sentence = ['I', 'love', 'Python'] 

def concatinate(word, words):
    return word + " " + words
result =reduce(concatinate, sentence)

print(result) 



from functools import reduce


def square(number):
    return number ** 2
    
def product(first_number,second_number):
    return first_number * second_number
    
square_list = list(map(square, [1, 2, 3, 4]))
print(square_list)
print(reduce(product,square_list))
