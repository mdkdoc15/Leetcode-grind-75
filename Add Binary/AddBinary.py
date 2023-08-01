# Created by matthewkight at 7/30/23
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        out = []
        carry_bit = 0
        while i >= 0 or j >= 0:
            a_val = b_val = 0
            if i >= 0:
                a_val = int(a[i])
            if j >= 0:
                b_val = int(b[j])
            add_val = a_val + b_val + carry_bit
            if add_val > 1:
                add_val -= 2
                carry_bit = 1
            else:
                carry_bit = 0
            i -= 1
            j -= 1
            out.append(str(add_val))
        if carry_bit:
            out.append('1')
        return "".join(out)[::-1]

if __name__ == '__main__':
    s = Solution()
    x = "11"
    y = "1"
    print(s.addBinary(x, y))
