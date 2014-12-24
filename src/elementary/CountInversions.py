__author__="mike"
__date__ ="$24-Dec-2014 12:01:18 AM$"

"""
    Count inversions in a sequence of numbers
"""
# Recursive solution 
__author__="McTpaxep"
def count_inversion_recursive(seq, k=0):
    seq=list(seq)
    for x in range(len(seq)-1):
        if seq[x]>seq[x+1]:
            seq[x],seq[x+1] = seq[x+1], seq[x]
            return count_inversion(seq, k+1)
    print(str(k))
    return k

# Non-recursive solution (modified bubble sort)
def count_inversion(sequence_tuple):
    inversion_count = 0
    sequence = list(sequence_tuple)
    for passnum in range(len(sequence)-1, 0, -1):
        for i in range(passnum):
            if sequence[i]>sequence[i+1]:
                inversion_count += 1
                temp = sequence[i]
                sequence[i] = sequence[i+1]
                sequence[i+1] = temp
    return inversion_count

if __name__ == '__main__':
    sequence_tuple = (5, 3, 2, 1, 0)
    print(count_inversion(sequence_tuple))
