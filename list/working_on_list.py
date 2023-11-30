# concatenation of string
animal = ['cart', 'dog']
wild_animal = ['tiger', 'fox']
animal += [wild_animal]
# print(animal)


# object
# Note - when you create a string , integer , float value , and list that is store as a object has assign id
print(id('string'))

# here also object is created and also assign the id but here variable greeting pointing that id
greeting = "hello"
print(id(greeting))

# and here concatenate with new string new object is created and store in greeting
greeting = greeting + " word!"
print(id(greeting))
