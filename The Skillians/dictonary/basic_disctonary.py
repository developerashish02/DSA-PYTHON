
# # update
# address.update({"name": "shubham", "phone_no": 8449618890})

# print(address)


def isPresent(address, key):
    for item in address:
        if item == key:
            print("key is present")
            return

    print("key is not present")


key = "age"
address = {
    "name": "Ashish",
    "surname": 9545959973,
    "age": 22,
    "city": 'kolhapur',
    "pin_code": 416113,
}
ans = isPresent(address, key)
