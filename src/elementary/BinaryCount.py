__author__="mike"
__date__ ="$27-Dec-2014 8:01:36 PM$"

"""
convert int to the binary format and count how many unities (1) are in the number spelling
"""
def checkio(number):
    return bin(number).count("1")
if __name__ == "__main__":
    print(checkio(15))   #== 4
    print(checkio(1))    #== 1
    print(checkio(1022)) #== 9
