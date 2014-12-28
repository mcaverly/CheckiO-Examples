__author__="mike"
__date__ ="$24-Dec-2014 2:33:35 PM$"

"""
    Determine if a suffix within a list exists at the end of any given word
"""
def checkio(words_set):
    for word in words_set:
            for suffix in words_set:
                if word.endswith(suffix) and word != suffix:
                    return True
    return False

if __name__ == '__main__':
    print(checkio({"hello", "lo", "he"}))
    print(checkio({"hello", "la", "hellow", "cow"}))
