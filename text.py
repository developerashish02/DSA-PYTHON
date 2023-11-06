

def findWords(str):
    spaces = 1

    for s in str:
        if s == ' ':
            spaces += 1

    return spaces


def mostWordsFound(sentences):

    if len(sentences) == 1:
        return 1

    if len(sentences) == 0:
        return 0

    maxWord = 0
    for index in range(len(sentences)):
        ans = findWords(sentences[index])

        if ans > maxWord:
            maxWord = ans

    return maxWord


sentences = []

ans = mostWordsFound(sentences)
print(ans)
