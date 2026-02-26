import random

QUESTIONS = [
    {
        "question": "Reverse a string.",
        "tests": [
            {"input": "hello", "output": "olleh"},
            {"input": "abc", "output": "cba"}
        ]
    },
    {
        "question": "Check prime number.",
        "tests": [
            {"input": "5", "output": "True"},
            {"input": "4", "output": "False"}
        ]
    },
    {
        "question": "Find factorial of number.",
        "tests": [
            {"input": "5", "output": "120"},
            {"input": "3", "output": "6"}
        ]
    },
    {
        "question": "Count vowels in string.",
        "tests": [
            {"input": "hello", "output": "2"},
            {"input": "xyz", "output": "0"}
        ]
    },
    {
        "question": "Find maximum number in list (space separated).",
        "tests": [
            {"input": "1 5 3", "output": "5"}
        ]
    },
    {
        "question": "Check palindrome string.",
        "tests": [
            {"input": "madam", "output": "True"},
            {"input": "hello", "output": "False"}
        ]
    },
    {
        "question": "Sum of digits of number.",
        "tests": [
            {"input": "123", "output": "6"}
        ]
    },
    {
        "question": "Count words in string.",
        "tests": [
            {"input": "hello world", "output": "2"}
        ]
    },
    {
        "question": "Return square of number.",
        "tests": [
            {"input": "4", "output": "16"}
        ]
    },
    {
        "question": "Find length of string.",
        "tests": [
            {"input": "hello", "output": "5"}
        ]
    }
]

def get_random_question():
    return random.choice(QUESTIONS)