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
