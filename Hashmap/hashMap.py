my_dict = {
    "Name": "Ashish Amar Gaikwad"
}


# Insert in dictionary
my_dict['age'] = 22

# update in dictionary
my_dict['age'] = 44
print(my_dict)

# access the value
print(my_dict['Name'])
print(my_dict['age'])


if 'age' in my_dict:
    print("Age key is present")

else:
    print("Not Present")
