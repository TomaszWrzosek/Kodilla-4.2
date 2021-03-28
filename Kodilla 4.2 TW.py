def ispalindrome(word):
    
    word = word.lower()
    word_no_space = word.replace(" ","")
    word_no_dot = word_no_space.translate({ord('.'): None})
    word_no_coma = word_no_dot.translate({ord(','): None})
    word_no_ask = word_no_coma.translate({ord('?'): None})
    word_no_interpunkcja = word_no_ask.translate({ord('!'): None})

    drow = word_no_interpunkcja[::-1]

    if word_no_interpunkcja == drow:
        return True
    else:
        return False
 
print(ispalindrome("A to kiwi zdziwi kota!!!!"))
