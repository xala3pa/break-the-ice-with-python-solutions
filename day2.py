"""
Question 4:

Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which
contains every number.Suppose the following input is supplied to the program:

34,67,55,33,12,98

Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""
import math


def generate_data():
    number_sequence = input("Please, input a sequence of comma-separated numbers: ")
    numbers_list = number_sequence.split(',')
    print(numbers_list)
    numbers_tuple = tuple(numbers_list)
    print(numbers_tuple)


generate_data()

"""
Question 5:

Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""


class ManageStrings:

    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input("Input the string: ")

    def print_string(self):
        print(self.s.upper())


str_object = ManageStrings()
str_object.get_string()
str_object.print_string()

"""
Question 6:

Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2*C*D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume 
the following comma separated input sequence is given to the program:

100,150,180
The output of the program should be:

18,22,24
Hints:
If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output 
received is 26.0, it should be printed as 26).In case of input data being supplied to the question, it should be 
assumed to be a console input.
"""


def function(d_value):
    C_VALUE = 50
    H_VALUE = 30
    return round(math.sqrt(2 * C_VALUE * float(d_value) / H_VALUE))


def calculate_formula() -> None:
    d_values = input("Input the values for D: ")

    print(*(function(d_value) for d_value in d_values.split(',')), sep=',')


calculate_formula()

"""
Question 7:

Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th 
row and j-th column of the array should be i*j.

Note: i=0,1.., X-1; j=0,1..,Y-1. 
Suppose the following inputs are given to the program: 3,5

Then, the output of the program should be:

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""


def generate_2_dimensional_array(x: int, y: int) -> None:
    print([[i * j for j in range(y)] for i in range(x)])


generate_2_dimensional_array(3, 5)

"""
Question 8:

Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated 
sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:

without,hello,bag,world
Then, the output should be:

bag,hello,without,world
"""


def order_words(sentence: str):
    print(*sorted(sentence.split(sep=',')), sep=',')


order_words("without,hello,bag,world")

"""
Question 9:
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

Hello world
Practice makes perfect
Then, the output should be:

HELLO WORLD
PRACTICE MAKES PERFECT
"""


def capitalize_sentences():
    capitalized_sentences = []
    while True:
        sentence = input()
        if len(sentence) == 0:
            break
        capitalized_sentences.append(sentence.upper())
    print(*capitalized_sentences, sep="\n")


capitalize_sentences()


def capitalize_sentences_v2():
    while True:
        string = input()
        if not string:
            return
        yield string


print(*(line.upper() for line in capitalize_sentences_v2()), sep='\n')
