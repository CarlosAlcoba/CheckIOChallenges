'''
def popular_words(text: str, words: list) -> dict:
    thisDict = {}
    text = text.lower().split()
    print(text)
    for i in words:
        count = text.count(i)
        thisDict[i] = count
    return thisDict



'''
print(11 ^ 9)