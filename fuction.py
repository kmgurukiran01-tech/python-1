def pillindrom(word):
    rev=""
    for i in range(len(word)-1,-1,-1):
        rev+=word[i]
    if rev==word:
        print(f"{rev} is pillindrom")
    else:
        print(f"{rev} is not pillindrom")
pillindrom("twoowt")
pillindrom("programer")