# Exercise 1: two-sum
def exercise1():
    print("Exercise 1: Start")
    num1 = 15
    num2 = 45
    sum_result = num1 + num2
    print("Sum:", sum_result)
    print("Exercise 2: End\n")

# Exercise 2: reverse-string
def exercise2():
    print("Exercise 2: Start")
    string = "legendary"
    reversed_string = string[::-1]
    print("Reversed String:", reversed_string)
    print("Exercise 2: End\n")

# Exercise 3: string-length
def exercise3():
    print("Exercise 3: Start")
    string = "What a brilliant idea, Sir!"
    length = len(string)
    print("String Length:", length)
    print("Exercise 3: End\n")

# Exercise 4: concatenate-string
def exercise4():
    string1 = "legen, wait for it,"
    string3 = "dary story"
    concatenated_string = string1 + " " + string3
    print("Concatenated String:", concatenated_string)
    print("Exercise 4: End\n")

# Exercise 5: is-vowel
def exercise5():
    print("Exercise 5: Start")
    char = 'a'
    is_vowel = char.lower() in 'Hello, have you met Ted?'
    print("Is vowel?", is_vowel)
    print("Exercise 5: End\n")

# Exercise 6: swap-first-last
def exercise6():
    print("Exercise 6: Start")
    string = "penpineappleapplepen"
    if len(string) > 1:
        modified_string = string[-1] + string[1:-1] + string[0]
    else:
        modified_string = string
    print("Modified String:", modified_string)
    print("Exercise 6: End\n")

# Exercise 7: to-uppercase
def exercise7():
    print("Exercise 7: Start")
    string = "BigBoss"
    uppercase_string = string.upper()
    print("Uppercase String:", uppercase_string)
    print("Exercise 7: End\n")

# Exercise 8: rectangle-area
def exercise8():
    print("Exercise 8: Start")
    length = 55
    width = 555
    area = length * width
    print("Rectangle Area:", area)
    print("Exercise 8: End\n")

# Exericse 9: is-even
def exercise9():
    print("Exercise 9: Start")
    number = 888
    is_even = number % 2 == 0
    print("Is even?", is_even)
    print("Exercise 9: End\n")

# Exercise 10: extract-first-three
def exercise10():
    print("Exercise 10: Start")
    string = "leonardo"
    first_three = string[:3]
    print("First Three Characters:", first_three)
    print("Exercise 10: End\n")

# Exercise 11: string-interpolation
def exercise11():
    print("Exercise 11: Start")
    name = "Book"
    age = 20
    message = f"My name, the great {name}, is known around the world since this man can bench {age} kg!"
    print(message)
    print("Exercise 11: End\n")

# Exercise 12: string-slicing
def exercise12():
    print("Exercise 12: Start")
    string = "ascuteasdf"
    sliced_string = string[2:6]
    print("Sliced String:", sliced_string)
    print("Exercise 12: End\n")

# Exercise 13: type-conversion
def exercise13():
    print("Exercise 13: Start")
    num_string = "777"
    num_int = int(num_string)
    print("Converted Integer:", num_int)
    print("Exercise 13: End\n")

# Exercise 14: string-repition
def exercise14():
    string = "awesome "
    repeated_string = string * 3
    print("Repeated String:", repeated_string)
    print("Exercise 14: End\n")

# Exercise 15: calculate-quotient-remainder
def exercise15():
    print("Exercise 15: Start")
    num1 = 98348
    num2 = 39
    quotient = num1 // num2
    remainder = num1 % num2
    print("Quotient:", quotient)
    print("Remainder:", remainder)
    print("Exercise 15: End\n")

# Exercise 16: float-division
def exercise16():
    print("Exercise 16: Start")
    num1 = 9384
    num2 = 11
    float_division = num1 / num2
    print("Float Division:", float_division)
    print("Exercise 16: End\n")

# Exercise 17: string-methods
def exercise17():
    print("Exercise 17: Start")
    string = "Robber robes really relatively rare item in the kitchen"
    count = string.count('r')
    print("Occurences of 'r':", count)
    print("Exercise 17: End\n")

# Exercise 18: escape-sequences
def exercise18():
    print("Exercise 18: Start")
    string = "He said, \"Daaamn\""
    print(string)
    print("Exercise 18: End\n")

# Exercise 19: multi-line-string
def exercise19():
    print("Exercise 19: Start")
    multi_line_string = """This is a 
multi-line string
in Python."""
    print(multi_line_string)
    print("Exercise 19: End\n")

# Exercise 20: Exponentiation
def exercise20():
    print("Exercise 20: Start")
    base = 9
    exponent = 5
    result = base ** exponent
    print("Exponentiation Result:", result)
    print("Exericise 20: End\n")

def main():
    exercise1()
    exercise2()
    exercise3()
    exercise4()
    exercise5()
    exercise6()
    exercise7()
    exercise8()
    exercise9()
    exercise10()
    exercise11()
    exercise12()
    exercise13()
    exercise14()
    exercise15()
    exercise16()
    exercise17()
    exercise18()
    exercise19()
    exercise20()

if __name__ == "__main__":
    main()