def is_palindrome(text):
    
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    return cleaned_text == cleaned_text[::-1]


example = "A man, a plan, a canal, Panama!"
result = is_palindrome(example)
if result:
    print(f'"{example}" is a palindrome!')
    
