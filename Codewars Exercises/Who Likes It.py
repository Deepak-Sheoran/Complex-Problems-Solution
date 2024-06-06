# Instructions

# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other
# items. We want to create the text that should be displayed next to such an item.
#
# Implement the function which takes an array containing the names of people that like an item. It must return the
# display text as shown in the examples:
#
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

# Solution
from code_checker import Checker


def likes(names):
    if len(names) <= 1:
        return f"{'no one' if len(names) == 0 else names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    else:
        option1 = f"{names[0]}, {names[1]}"
        option2 = f"{names[2] if len(names) == 3 else f'{len(names) - 2} others'}"
        return f"{option1} and {option2} like this"


test_cases = \
    [
        {"input": [], "answer": 'no one likes this'},
        {"input": ['Peter'], "answer": 'Peter likes this'},
        {"input": ['Jacob', 'Alex'], "answer": 'Jacob and Alex like this'},
        {"input": ['Max', 'John', 'Mark'], "answer": 'Max, John and Mark like this'},
        {"input": ['Alex', 'Jacob', 'Mark', 'Max'], "answer": 'Alex, Jacob and 2 others like this'}
    ]

for test_case in test_cases:
    checker = Checker(likes(test_case['input']), test_case['answer'])
    print(checker.check())
