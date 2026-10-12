
print("\nQ1a\n")
#Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a: I used slicing to select and print the first five elements.
print(x[:5])


print("\nQ1b\n")
# Q1b: Print only the even numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

#A1b: I used a for loop and the modulo operator to print only even numbers.
for number in x:
    if number % 2 == 0:
        print(number)


print("\nQ1c\n")
# Q1c: Print the even numbers up to the fifth element
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c: I combined slicing and a for loop to print even numbers from the first five elements.
for number in x[:5]:
    if number % 2 == 0:
        print(number)


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: Create a list containing the first letter of each first name
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson",
         "Annie Easley", "Terence Tao"]

# A2a: I used a for loop and string indexing to collect the first initial of each name.
first_initials = []

for name in names:
    first_initials.append(name[0])
print(first_initials)


print("\nQ2b\n")
# Q2b: Create a list containing the index of the space in each name
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson",
         "Annie Easley", "Terence Tao"]

# A2b: I used the index method to find the position of the space in each name.
space_positions = []

for name in names:
    space_positions.append(name.index(" "))
print(space_positions)


print("\nQ2c\n")
# Q2c: Create a list containing the first and last initial of each person
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson",
         "Annie Easley", "Terence Tao"]

# A2c: I used string indexing to extract and combine the first and last initials.
initials = []

for name in names:
    space_position = name.index(" ")
    first_initial = name[0]
    last_initial = name[space_position + 1]
    initials.append(first_initial + last_initial)

print(initials)


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Print only the lists that have no duplicates
list_of_lists = [
    [1, 5, 7, 3, 44, 4, 1],
    ["A", "B", "C"],
    ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
    ["one", "Two", "Three", "Four"]
]

# A3a: I used sets to identify and print only the lists without duplicates.
for sublist in list_of_lists:
    if len(sublist) == len(set(sublist)):
        print(sublist)


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Ask the user for a number greater than 100 and repeat until valid.

# A4a: I used a while loop to keep asking for input until the number is greater than 100.
number = int(input("Enter a number greater than 100: "))

while number <= 100:
    number = int(input("Try again. Enter a number greater than 100: "))

print(number)


print("\nQ4b\n")
# Q4b: Print "prime" if the number is prime, otherwise print "not prime".

# A4b: I used a for loop and modulo to check for divisors and determine whether the number is prime.
is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break

if is_prime:
    print("prime")
else:
    print("not prime")