def checkio(words):
    alpha_count = 0
    if len(words) > 0 and len(words) < 100:
        for word in words.split(" "):
            if word.isalpha() == True:
                alpha_count += 1
                if alpha_count >= 3:
                    return True
            elif word.isdecimal() == True:
                alpha_count = 0
        return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
