def alphabet_position(letter):
    letter = letter.lower()
    aValue = ord(letter)
    locLetter = aValue - 97
    return locLetter

def rotate_character(letter, rot):
    aLoc = alphabet_position(letter)
    rLoc = ((aLoc + rot) % 26) + 97
    return chr(rLoc)

def encrypt(text, rot):
    finalText = ""
    rotInt = int(rot)

    for ch in text:
        wasupper = ch.isupper()
        if ch.isalpha():
            a = rotate_character(ch, rotInt)
            if wasupper:
                a = a.upper()
            finalText += a
        else:
            finalText += ch
    return finalText
