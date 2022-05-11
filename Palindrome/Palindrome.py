# Created by matthewkight at 5/11/22

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_string = ""
        s = s.upper()
        for char in s:
            if char.isalnum():
                alpha_string += char
        rev_str = alpha_string[::-1]
        return alpha_string == rev_str

if __name__ == '__main__':
    sol = Solution()
    sol.isPalindrome("0A man, a plan, a canal: Panama")
