def is_pangram(sentence):
    sentence = sentence.lower()
    letters = ""
    for character in sentence:
        if character.isalpha():
            letters += character
    return len(set(letters)) == 26
    
