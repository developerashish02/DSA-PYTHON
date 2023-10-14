
def searchInString(name, charFind):
    if len(name) == 0:
        return False

    for index in range(len(name)):
        if name[index] == charFind:
            return True

    # This Line Executed means we do not find  the character
    return False


name = "Ashish"
charFind = '0'

ans = searchInString(name, charFind)
print(ans)
