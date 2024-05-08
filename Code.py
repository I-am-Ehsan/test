"""
import re

def contains_numbers_and_letters(text):
    # Define a regex pattern to match both numbers and letters
    pattern = r'(\d*[a-zA-Z]\d*)+@[a-zZ-a]+(.com)$'

    # Use the re.search function to check if the pattern matches the text
    if re.search(pattern, text):
        return True
    else:
        return False

# Example usage:
text1 = "e@gmail.com"  # Contains both letters and numbers
text2 = "123"     # Contains only numbers
text3 = "abc"     # Contains only letters

print(contains_numbers_and_letters(text1))  # Output: True
print(contains_numbers_and_letters(text2))  # Output: False
print(contains_numbers_and_letters(text3))  # Output: False

"""