# Instructions
#
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def insert_values(values):
    """
    Function for changing an iterable into a linked list object and returning the first node object through which all
    the remaining nodes can be accessed.
    :param values:
    :return: a ListNode Object
    """
    head = ListNode(values[0])
    itr = head
    for value in values[1:]:
        itr.next = ListNode(value)
        itr = itr.next

    return head


def add_two_numbers(l1, l2):
    """
    Approach behind the solution:-
    1. First of all access all the data in the two list nodes object and store them in a list.
    Note - Inserting the values at index 0 is not efficient since the time complexity for inserting an item via .insert
    method comes out to be O(n) while appending is O(1)
    2. Reverse the list since the number in the linked lists are stored in reverse order. Next join the numbers in the
    list using the .join() method and change the data type to int.
    3. Add the two numbers and then change the resulting number in a string and then reverse it.
    4. Last step is to iterate through the string while changing the numbers into int and store the values in a linked
    list and return the head node that contains the first node of the list.
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    num1 = []
    num2 = []
    while l1 is not None or l2 is not None:
        if l1 is not None:
            num1.append(str(l1.val))
            l1 = l1.next
        if l2 is not None:
            num2.append(str(l2.val))
            l2 = l2.next
    num1.reverse()
    num2.reverse()
    num1 = int("".join(num1))
    num2 = int("".join(num2))
    num = str(num1 + num2)
    head = ListNode(int(num[0]), None)
    itr = head
    for n in num[1:]:
        itr.next = ListNode(int(n))
        itr = itr.next
    return head


L1 = insert_values([0, 8, 8, 8, 8, 2, 9, 3, 1, 1])
L2 = insert_values([0, 9, 1, 5, 5, 5, 1, 1, 6])
# L1 = insert_values([0])
# L2 = insert_values([0])
L = add_two_numbers(L1, L2)
while L is not None:
    print(L.val, end="")
    L = L.next
