# 1. Prime Number Sum Calculator
def prime_sum(start, end):
    def prime_num(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    prime_sum = 0
    for num in range(start, end + 1):
        if prime_num(num):
            prime_sum += num
    return prime_sum

# 2. Length Unit Converter
def length_converter(value, direction):
    if direction == 'M':
        return round(value * 3.28084, 2)  # meters to feet
    elif direction == 'F':
        return round(value / 3.28084, 2)  # feet to meters
    else:
        return "Invalid direction. Use 'M' or 'F'."

# 3. Consonant Counter
def consonant_counter(text):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    consonant_count = 0
    for char in text:
        if char in consonants:
            consonant_count += 1
    return consonant_count

# 4. Min-Max Number Finder
def min_max_finder(*numbers):
    """Find the minimum and maximum numbers from a list of inputs."""
    if len(numbers) == 0:
        return "No numbers provided."
    smallest = largest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return f"Smallest: {smallest}, Largest: {largest}"

# 5. Palindrome Checker
def palindrome_checker(text):
    """Check if a given string is a palindrome."""
    cleaned_text = ''
    for char in text:
        if char.isalnum():
            cleaned_text += char.lower()
    return cleaned_text == cleaned_text[::-1]

# 6. Word Counter
def word_counter(filename):
    words_to_count = ["the", "was", "and"]
    word_count = {}

    for word in words_to_count:
        word_count[word] = 0

    with open(filename, 'r') as file:
        text = file.read().lower()
        words = text.split()

        for word in words:
            for x in word_count:
                if word == x:
                    word_count[x] += 1

    return word_count

def main():
    while True:
        print("Select a function (1-6):")
        print("1. Calculate the sum of prime numbers")
        print("2. Convert length units")
        print("3. Count consonants in string")
        print("4. Find min and max numbers")
        print("5. Check for palindrome")
        print("6. Word Counter")
        print("0. Exit program")

        choice = input("Enter your choice: ")

        if choice.isdigit() and 0 <= int(choice) <= 6:
            choice = int(choice)
        else:
            print("Invalid input. Please enter a number between 0 and 6.")
            continue

        for i in range(1, 7):
            if choice == i:
                break
        else:
            if choice == 0:
                print("Exiting the program.")
                break

        if choice == 1:
            # Prime Number Sum Calculator
            start = input("Enter the start range: ")
            end = input("Enter the end range: ")

            # Ensure both inputs are numeric
            if start.isdigit() and end.isdigit():
                start = int(start)
                end = int(end)
                sum = prime_sum(start, end)
                print(
                    f"The total sum of prime numbers within the specified range ({start}, {end}) is:  {sum}")
            else:
                print("Invalid input!. Please enter integer values.")
                continue

        elif choice == 2:
            # Length Unit Converter
            value = input("Enter the value: ")
            direction = input(
                "Enter direction (M for meters to feet, F for feet to meters): ").upper()

            # Ensure value is numeric and direction is valid
            if value.replace('.', '', 1).isdigit() and direction in ['M', 'F']:
                value = float(value)
                result = length_converter(value, direction)
                print(f"Converted value: {result} units")
            else:
                print(
                    "Invalid input. Please enter a valid numeric value and direction (M/F).")
                continue

        elif choice == 3:
            # Consonant Counter
            text = input("Enter a string: ")
            result = consonant_counter(text)
            print(f"Number of consonants: {result}")

        elif choice == 4:
            # Min-Max Number Finder
            numbers = input("Enter numbers separated by comma: ").split(',')

            all_numeric = True
            processed_numbers = []
            for num in numbers:
                num = num.strip()  # Remove any extra spaces
                if num.replace('.', '', 1).lstrip('-').isdigit():  # Check if it's a valid number (including negative and floating-point)
                    processed_numbers.append(float(num))  # Convert to float to handle both integers and decimals
                else:
                    all_numeric = False
                    break

            if all_numeric:
                result = min_max_finder(*processed_numbers)
                print(result)
            else:
                print("Invalid input. Please enter numeric values separated by commas.")
                continue

        elif choice == 5:
            # Palindrome Checker
            text = input("Enter a string: ")
            result = palindrome_checker(text)
            print(f"Is the string a palindrome? {result}")

        elif choice == 6:
            # Word Counter
            filename = input("Enter the filename: ")
            result = word_counter(filename)
            print(f"Word counts: {result}")

        continue_choice = input(
            "Would you like to try another function? (y/n): ").lower()

        if continue_choice == 'y':
            continue
        elif continue_choice == 'n':
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

main()