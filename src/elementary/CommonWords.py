__author__="mike"
__date__ ="$29-Dec-2014 4:58:00 PM$"

def checkio(first, second):
    common_words = []
    for first_word in first.replace(",", " ").split():
        for second_word in second.replace(",", " ").split():
            if first_word == second_word:
                common_words.append(first_word)
    return " ".join(sorted(common_words))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio("hello,world", "hello,earth")) #== "hello", "Hello"
    print(checkio("one,two,three", "four,five,six")) #== "", "Too different"
    print(checkio("one,two,three", "four,five,one,two,six,three")) #== "one,three,two", "1 2 3"
