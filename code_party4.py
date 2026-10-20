languages = ['python', 'java', 'c++']

def to_uppercase(word):
    return word[0].upper() + word[1:] if word[0].islower() else word
result = list(map(to_uppercase, languages))
print (result)




numbers = range(1, 11)

def square(value):
    return value **2 
result = list(map(square, numbers))
print(result)



names = ['john', 'mary', 'steve']

def capitalize_letter(word):
    return word[0].upper() + word[1:] if word[0].islower() else word
words = list(map( capitalize_letter, names))
print(words)



prices = [100, 200, 300]

def add_ten_percent(price):
    return price*1.10
cost = list(map(add_ten_percent ,prices))

print(cost)




