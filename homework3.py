def words2characters(words):
    characters = []

    for word in words:
        word = str(word)

        for character in word:
            characters.append(character)

    return characters
