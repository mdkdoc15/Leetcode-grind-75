# Created by matthewkight at 7/28/23
from collections import deque

class Solution:
    def longestPalindrome(self, s: str) -> int:
        num_of_let = {}
        for ch in s:
            num_of_let[ch] = num_of_let.get(ch, 0) + 1

        used_odd = False
        total_len_pal = 0
        for num in num_of_let.values():
            if num % 2 == 0:
                total_len_pal += num
            else:
                total_len_pal += num - 1
                used_odd = True
        total_len_pal += int(used_odd)
        return total_len_pal

if __name__ == '__main__':
    sol = Solution()
    st = "bananas"
    print(sol.longestPalindrome(st))
