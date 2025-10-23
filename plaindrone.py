def is_palindrome(text):
  # Clean the input: remove non-alphanumeric and convert to lowercase
  cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
  # Compare the cleaned string with its reverse
  return cleaned_text == cleaned_text[::-1]

# Example usage:
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False
print(is_palindrome("Racecar")) # Output: True
print(is_palindrome("A man, a plan, a canal: Panama")) # Output: True