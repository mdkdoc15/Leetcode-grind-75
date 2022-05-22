# Created by matthewkight at 5/22/22


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1

        for char in t:
            val = dic.get(char, 0)
            if val != 0:
                dic[char] -= 1
            else:
                return False

        return len(s) == len(t)



if __name__ == '__main__':
    pass
