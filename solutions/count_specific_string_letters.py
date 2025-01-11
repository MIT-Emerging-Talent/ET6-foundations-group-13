"""
A function that counts a specific string letters in a sentence using the count method.

function contents -
    count_string = a function that counts the occurrence of a specific letter in a given sentence or phrase.

 created on 07 Jan 2025
 @author: Hope Udoh


"""


def count_string(sentence: str, letters: str) -> str:
    """
    This function counts the occurrence of a specific letter in a given sentence.

    Parameters:
    sentence (str): The input sentence where the letter count will be performed.
    letters (str): The specific letter to count its occurrence in the sentence.

    Returns:
    str: A string indicating the count of the specific letter in the sentence.

    Raises:
        ValueError: If the letters parameter is an empty string.

    Example 1:
    >>> count_string("hello", "l")
    'the letter 'l' appears 2 times'

    Example 2:
    >>> count_string("I love pineapples too much", "t"))
    'the letter 't' appears 1 times'
    
    Example 3:
    >>> count_string("Hope", "x"))
    'the letter 'x' appears 0 times'

    """
    if not letters:
        raise ValueError("The letter to count must not be empty.")

    specific_letter_count = sentence.count(letters)
    return f"The letter '{letters}' appears {specific_letter_count} times"

