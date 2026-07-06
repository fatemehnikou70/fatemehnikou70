def is_isogram(phrase):
    phrase=phrase.lower()
    phrase = phrase.replace("-","").replace(" ","")
    if len(phrase) == len(set(phrase)):
        return True
    else:
        return False
    
    
    
