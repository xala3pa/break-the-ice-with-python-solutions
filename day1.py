"""
Question 1:

Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000
and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.
"""


def find_numbers():
    for number in range(2000, 3201):
        if number % 7 == 0 and number % 5 != 0:
            print(number, end=',')


def find_numbers_v2():
    print(*[number for number in range(2000, 3201) if number % 7 == 0 and number % 5 != 0], sep=',')


find_numbers_v2()

"""
Question 2:

Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated 
sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320
"""


def compute_factorial():
    number = int(input("which number do you want to calculate its factorial? : "))
    acc = 1
    for i in range(1, number + 1):
        acc *= i
    return acc


def factorial_recursive(num: int) -> int:
    return 1 if num <= 1 else num * factorial_recursive(num - 1)


def compute_factorial_recursive():
    number = int(input("Which number do you want to calculate its factorial? : "))
    result = factorial_recursive(number)
    return result


print(compute_factorial_recursive())

"""
Question 3:

With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an 
integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following 
input is supplied to the program: 8
Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""


def generate_dict(number: int):
    return {i: i * i for i in range(1, number + 1)}


print(generate_dict(8))
