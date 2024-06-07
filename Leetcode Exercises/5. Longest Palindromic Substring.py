# Instructions:-
# Given a string s, return the longest palindromic substring in s.

def is_palindrome(substring):
    if substring == substring[::-1]:
        return True
    return False


class Solution:
    def __init__(self, s):
        self.string = s
        self.sol = self.longest_palindrome()

    def longest_palindrome(self):
        """
        Approach:-
        Basically what I am doing is going from 1 to the max length of the existing palindrome within the string
        First, a number is decided by the first enclosing loop i.e., the for loop. The number keeps increasing once a
        palindrome is found or not, if a palindrome is found matching that number then we assign that number to
        max length and increase the number. like this we traverse the whole string taking subsets of the string each
        time and increasing their length every time.
        :return: The length of the longest palindrome within the provided string
        """
        max_length = 0
        l = len(self.string)
        longest_palindrome = ""
        for i in range(1, l+1):
            j = 0
            k = i
            while k <= l:
                if is_palindrome(self.string[j:k]):
                    if k - j > max_length:
                        max_length = k - j
                        longest_palindrome = self.string[j:k]
                        break
                k += 1
                j += 1
        print(longest_palindrome)
        return max_length


sol = Solution(
    "wgjtmwgpfnoeisdozatlhfvcqzlsffkoxrsdjhryqtppdeqrkjabodgtmkthwmtmerxlazsfdogsrwtswhbqclpcagfjlfuyvsnummf"
    "jmmxpdhupwkztnwcbppbbwfnwfaoazmautdiutzkwfqibglhypfamgxzsfctapkjimmyazulehprmzfvhaxzbobhvsbxscimjnmibiv"
    "wbenfrhsudmpmkkbphjyrgjficjvfosrnhdsnjqtaycmyorpujyloozeeinqfsesuauqmsxmoafoszqrzbgechluecfdxulmcxxbiqv"
    "qkohlgqlqxierzbyradeoebbdhyjdkiaezfphfetiyelelunryvmczewjwkfrgjvdbouorqymmamkonncostamlpyrxoxnccbilnqdq"
    "beieqncitfgitluvzxildtsiaipbskicepbvhtfdgxfiyywznzdstzvayjmwvlolhtvpekyakajeixdjkbbdlttldbbkjdxiejakayk"
    "epvthlolvwmjyavztsdznzwyyifxgdfthvbpeciksbpiaistdlixzvultigfticnqeiebqdqnlibccnxoxryplmatsocnnokmammyqr"
    "ouobdvjgrfkwjwezcmvyrnuleleyitefhpfzeaikdjyhdbbeoedarybzreixqlqglhokqvqibxxcmluxdfceulhcegbzrqzsofaomxs"
    "mquausesfqnieezoolyjuproymcyatqjnsdhnrsofvjcifjgryjhpbkkmpmdushrfnebwvibimnjmicsxbsvhbobzxahvfzmrpheluz"
    "aymmijkpatcfszxgmafpyhlgbiqfwkztuidtuamzaoafwnfwbbppbcwntzkwpuhdpxmmjfmmunsvyufljfgacplcqbhwstwrsgodfsz"
    "alxremtmwhtkmtgdobajkrqedpptqyrhjdsrxokffslzqcvfhltazodsieonfpgwmtjgw")
print(sol.sol)
