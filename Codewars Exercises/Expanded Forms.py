# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:
#
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'

def expanded_form(nums):
    nums = list(str(nums))
    ans = []
    l = len(nums)
    for n in nums:
        if n == "0":
            l -= 1
            pass
        else:
            ans.append(str(int(n) * (10 ** (l - 1))))
            l -= 1
    return " + ".join(ans)


# Another function that can get the job done
def expanded_form1(number):
    enum = list(enumerate(list(str(number))[::-1]))
    ans = [str(int(value) * (10 ** power)) for power, value in enum[::-1] if value != "0"]
    return " + ".join(ans)


def proper_print(number):
    print(f"Expanded form of {number} = {expanded_form(number)}")


nums = [12, 42, 70304, 93505, 87080]

for num in nums:
    proper_print(num)
