numbers = range(1,21)

def number(value):

    return value % 2 == 0
result = list(filter(number, numbers))
print(result)




def character_length(words):
    word_list = []
    for word in words:
        if len(word) >= 5:
            word_list.append(word)

    return word_list

words = ( ['cat', 'elephant', 'tiger', 'lion'])
print(character_length(words))




datas = [(1, 'A'), (4, 'B'), (2, 'C')]


def data(value):
    return value[0] > 2
result = list(filter(number, numbers))

print(result)



numbers = range(1, 51)

def divisible(value):
    return value % 3 == 0 and value % 5 == 0
result = list(filter(divisible, numbers))
print(result)




words = ['level', 'world', 'madam', 'python']

def palindrome(word):
    return word == word[::-1]
result = list(filter(palindrome,words))
print(result)









