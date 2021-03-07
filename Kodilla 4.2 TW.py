def ispalindrome(word):
    
    word = word.lower()
    drow = word[::-1]

    if word == drow:
        return True
    else:
        return False
 
print(ispalindrome("ajajajaja"))