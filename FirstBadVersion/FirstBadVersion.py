# Created by matthewkight at 9/29/22

def isBadVersion(val):
    return val >= 2

def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    max_val = n
    min_val = 0
    cur_val = (n + 1) // 2
    while True:
        if max_val == min_val:
            return max_val + 1
        if not isBadVersion(cur_val):
            # The version is later in the call
            min_val = cur_val + 1
        else:
            # Version is closer in the call
            max_val = cur_val - 1
            if max_val <= min_val:
                return cur_val

        cur_val = (min_val + max_val) // 2


if __name__ == '__main__':
    print(firstBadVersion(3))
