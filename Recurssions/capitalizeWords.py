def capitalizeWords(wordsArray):
    resultArray =[]

    if len(wordsArray)==0:
        return resultArray

    resultArray.append(wordsArray[0].upper())

    return resultArray +  capitalizeWords(wordsArray[1:])

print(capitalizeWords(['taranjeet','singh','mundhan']))