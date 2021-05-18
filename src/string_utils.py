def is_palindrome(phrase: str) -> bool:
    lower = phrase.lower().replace(' ', '')
    reverse = lower[::-1]

    return reverse == lower
