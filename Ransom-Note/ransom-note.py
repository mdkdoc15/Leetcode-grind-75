# Created by matthewkight at 7/24/23

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_letters = {}
        # Track how many of each letter we have
        for letter in magazine:
            mag_letters[letter] = mag_letters.get(letter, 0) + 1
        # Remove letters one by one
        for letter in ransomNote:
            mag_letters[letter] = mag_letters.get(letter, 0) - 1
            if mag_letters[letter] < 0:
                return False
        return True
if __name__ == '__main__':
    s = Solution()
    ran = "aa"
    mag = "aab"
    print(s.canConstruct(ransomNote=ran, magazine=mag))
