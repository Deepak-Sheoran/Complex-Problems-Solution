# Instructions

# There is a queue for the self-checkout tills at the supermarket. Your task is to write a function to calculate the
# total time required for all the customers to check out!

# input customers: an array of positive integers representing the queue. Each integer represents a customer,
# and its value is the amount of time they require to check out. n: a positive integer, the number of checkout tills.
# output The function should return an integer, the total time required.

from code_checker import Checker


def queue_time(customers, n):
    tills = [0] * n
    for customer_time in customers:
        i = tills.index(min(tills))
        tills[i] += customer_time
    return max(tills)


test_cases = \
    [
        {"input": ([], 1), "answer": 0},
        {"input": ([5], 1), "answer": 5},
        {"input": ([2], 5), "answer": 2},
        {"input": ([1, 2, 3, 4, 5], 1), "answer": 15}
    ]

for test_case in test_cases:
    checker = Checker(queue_time(test_case['input'][0], test_case['input'][1]), test_case['answer'])
    print(checker.check())

# test.assert_equals(queue_time([1, 2, 3, 4, 5], 100), 5, "wrong answer for a case with a large number of tills")
# test.assert_equals(queue_time([2, 2, 3, 3, 4, 4], 2), 9, "wrong answer for a case with two tills")
