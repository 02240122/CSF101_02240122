# Function 1: Prime Number Sum Calculator
def prime_sum(start, end):
    """Calculate the sum of prime numbers between start and end."""
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    prime_sum = 0
    for num in range(start, end + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum

# Function 2: Length Unit Converter
def length_converter(value, direction):
    """Convert between meters and feet."""
    if direction == 'M':
        return round(value * 3.28084, 2)  # meters to feet
    elif direction == 'F':
        return round(value / 3.28084, 2)  # feet to meters
    else:
        return "Invalid direction. Use 'M' or 'F'."

# Function 3: Consonant Counter
def consonant_counter(text):
    """Count the consonants in a given string."""
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    consonant_count = 0
    for char in text:
        if char in consonants:
            consonant_count += 1
    return consonant_count

# Function 4: Min-Max Number Finder
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

# Function 5: Palindrome Checker
def palindrome_checker(text):
    """Check if a given string is a palindrome."""
    cleaned_text = ''
    for char in text:
        if char.isalnum():
            cleaned_text += char.lower()
    return cleaned_text == cleaned_text[::-1]

# Function 6: Word Counter
def word_counter(filename):
    """Count specific words in a text file."""
    words_to_count = ["the", "was", "and"]
    word_count = {}
    
# Initialize count for each word in the words_to_count list
    for word in words_to_count:
        word_count[word] = 0

    # Check if the file exists
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()
            words = text.split()
            
            # Count each word manually (without using list comprehension or map)
            for word in words:
                for key in word_count:
                    if word == key:
                        word_count[key] += 1
    except FileNotFoundError:
        return "File not found."

    return word_count

# Main program
def main():
    while True:
        # Display the menu
        print("Select a function (1-6):")
        print("1. Calculate the sum of prime numbers")
        print("2. Convert length units")
        print("3. Count consonants in string")
        print("4. Find min and max numbers")
        print("5. Check for palindrome")
        print("6. Word Counter")
        print("0. Exit program")
   
   