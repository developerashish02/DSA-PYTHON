

def remove_a(string, index, output):
    # base case
    if index == len(string):
        return output

    # check if character is a or not
    if string[index] != 'a':
        output += string[index]

    return remove_a(string, index + 1, output)


# in the string apple is present skip the word
def is_starts_with_apple(string, index, output):
    # base case
    if index == len(string):
        return output

    # recursion call
    # if substring contains apple skip the word
    substring = string[index:]
    if substring.startswith("apple"):
        return is_starts_with_apple(string, index + 5, output)

    # if apple not contains added to the ans
    else:
        output += string[index]
        return is_starts_with_apple(string, index + 1, output)


# if word is not apple then only remove word app
def skip_app_not_starts_with_apple(string, index, output):
    # base case
    if index == len(string):
        return output

    # recursion call
    # if substring contains apple skip the word
    substring = string[index:]
    if substring.startswith("app") and not substring.startswith("apple"):
        return skip_app_not_starts_with_apple(string, index + 3, output)

    # if apple not contains added to the ans
    else:
        output += string[index]
        return skip_app_not_starts_with_apple(string, index + 1, output)


string = "appbananaapple"
ans = skip_app_not_starts_with_apple(string, 0, "")
print(ans)


# string = "aashish"
# ans = remove_a(string, 0, "")
# print(ans)
