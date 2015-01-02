__author__="mike"
__date__ ="$29-Dec-2014 5:27:05 PM$"

"""
Sort a tuple input into ascending order based on absolute value
"""

def checkio(numbers_array):
    abs_array = []
    sorted_array = []
    
    for value in numbers_array:
        abs_array.append(abs(value))
        
    for abs_value in sorted(abs_array):
        for value in numbers_array:
            if abs(value) == abs_value:
                sorted_array.append(value)
    return sorted_array

if __name__ == "__main__":
    
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)
    
    print(check_it(checkio((-20, -5, 10, 15)))) #== [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    print(check_it(checkio((1, 2, 3, 0)))) #== [0, 1, 2, 3], "Positive numbers"
    print(check_it(checkio((-1, -2, -3, 0)))) #== [0, -1, -2, -3], "Negative numbers"
