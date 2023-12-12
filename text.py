def skip_app_not_starts_with_app_not_starts_with_apple(string, index, output):
    # base case
    if index == len(string):
        return output

    # recursion call
    # if substring contains "app" but does not start with "apple", skip the word
    substring = string[index:]
    if substring.startswith("app") and not substring.startswith("apple"):
        return skip_app_not_starts_with_app_not_starts_with_apple(string, index + 3, output)

    # if "apple" is not found, add the character to the output
    else:
        output += string[index]
        return skip_app_not_starts_with_app_not_starts_with_apple(string, index + 1, output)


# Example usage
string = "appbananaapple"
ans = skip_app_not_starts_with_app_not_starts_with_apple(string, 0, "")
print(ans)
