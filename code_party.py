numbers = range(1,51)

def sum_of_number(value)
    return sum(range(1,51))

total = reduce(sum_of_number, numbers)
print(total)
