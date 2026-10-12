
print("\nQ1a\n")
# Q1a: Write a function that returns all divisors of an integer.

# A1a: I used a for loop and modulo to find all numbers that divide the integer without a remainder.
def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
print(get_divisors(12))


print("\nQ1b\n")
# Q1b: Return True if one integer is a factor of the other, False otherwise.

# A1b: I reused my previous function to check whether either number is a factor of the other.
def is_factor(a, b):
    if a == 0 or b == 0:
        return False
    return a in get_divisors(abs(b)) or b in get_divisors(abs(a))
print(is_factor(3, 12))
print(is_factor(5, 12))


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: Return the position of a letter in the alphabet.

# A2a: I used a list of letters and the index method to find each letter's alphabet position.
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

def letter_position(letter):
    letter = letter.lower()
    return alphabet.index(letter) + 1
print(letter_position("a"))
print(letter_position("b"))
print(letter_position("z"))


print("\nQ2b\n")
# Q2b: Create an ID using the alphabet positions of each letter in a name.

# A2b: I looped through each letter, found its alphabet position and joined the positions into a string.
def create_id(name):
    name = name.lower()
    id_number = ""
    for letter in name:
        id_number += str(letter_position(letter))
    return id_number

print(create_id("bob"))
print("\nQ2c\n")
# Q2c: Create a password by subtracting the sum of the ID digits from the ID.

# A2c: I reused the ID function, added its digits together and subtracted their total from the ID.
def create_password(name):
    id_number = create_id(name)
    total = sum(int(digit) for digit in id_number)
    password = int(id_number) - total
    return password
print(create_password("bob"))


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Return True if an integer is prime and False otherwise.

# A3a: I checked whether any number between 2 and the given integer divides it without a remainder.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(7))
print(is_prime(9))


print("\nQ3b\n")
# Q3b: Handle input that is not a valid whole number.

# A3b: I used try and except to handle invalid input and reused my prime-checking function.
def check_prime_input(value):
    try:
        n = int(value)
    except (ValueError, TypeError):
        return "Please enter a valid whole number."
    return is_prime(n)
print(check_prime_input("7"))
print(check_prime_input("hello"))
print(check_prime_input("9"))