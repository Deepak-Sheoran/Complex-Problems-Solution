# Instruction
# Given a strings, find the length of the longest substring without repeating characters.

# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:

    def __init__(self, string):
        self.str = string
        self.length_of_longest_substring()

    def length_of_longest_substring(self):
        """
        There are two approach that can be followed to do this,
        In the first approach:-
        Create a list seen that will keep record of the unique strings taken from the input string. If a string is
        repeated then we start to keep the string after the repeated string and remove it and the elements before it
        from the list. We also keep record of the length of the current list and the max length of the longest substring
        and if at any instance the length of the list if greater than the max length we update its value.
        :return: the length of the longest substring
        """
        seen = []
        max_length = 0
        num = 0
        for s in self.str:
            if s not in seen:
                seen.append(s)
                num += 1
                if num > max_length:
                    max_length = num
            else:
                seen = seen[seen.index(s)+1:]
                seen.append(s)
                num = len(seen)
        print("".join(seen))
        return max_length
        # longest = ""
        # second_longest = ""
        # for _ in self.str:
        #     if second_longest == "":
        #         if _ not in longest:
        #             longest += _
        #         else:
        #             second_longest = _
        #     else:
        #         if len(second_longest) > len(longest):
        #             longest = second_longest
        #             second_longest = ""
        #         if _ not in second_longest:
        #             second_longest += _
        #         else:
        #             second_longest = _
        # if len(second_longest) > len(longest):
        #     longest = second_longest
        #     second_longest = ""
        # print(longest)
        # return len(longest)


sol = Solution("abcdeabcdef")
