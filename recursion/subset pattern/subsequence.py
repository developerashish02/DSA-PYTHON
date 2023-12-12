def print_subsequence_return(p, up, index):
    # base condition
    if index == len(up):
        ans = []
        ans.append(p)
        return ans

    # first take the character at current index
    leftAns = print_subsequence_return(p + up[index], up, index + 1)
    # then skip the character at current index
    rightAns = print_subsequence_return(p, up, index + 1)

    leftAns += rightAns

    return leftAns


def print_subsequence(p, up, index):
    # base condition
    if index == len(up):
        print(p)
        return

    # first take the character at current index
    print_subsequence(p + up[index], up, index + 1)
    # then skip the character at current index
    print_subsequence(p, up, index + 1)


def print_subsequence_ASCII(p, up, index):
    # base condition
    if index == len(up):
        print(p)
        return

    # first take the character at current index
    print_subsequence_ASCII(p + up[index], up, index + 1)
    # then skip the character at current index
    print_subsequence_ASCII(p, up, index + 1)
    # for the ascii value
    print_subsequence_ASCII(p + str(ord(up[index])), index + 1)


string = "abc"
ans = print_subsequence_ASCII("", string, 0)
print(ans)
