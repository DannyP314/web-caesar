import string
def alphabet_position(letter):
    import string
    x = list(string.ascii_lowercase)
    for i in range(len(x)):
        if x[i] == letter.lower():
            return i

def rotate_character(char, rot):
    import string
    i = list(string.ascii_uppercase) #list of uppers
    x =list(string.ascii_lowercase) #list of lowers
    c = alphabet_position(char)
    new_pos = (c + rot) % 26

    if char in i:
        n = x[new_pos]
        n = n.upper()
        return n
    return x[new_pos]

def encrypt(text,rot):
    new_st = ""
    punc = string.punctuation
    dig = string.digits
    for i in text:
        if i in punc or i in dig or ord(i) == 32:
            new_st += i
        else:
            i = rotate_character(i, rot)
            new_st += i
    return new_st
