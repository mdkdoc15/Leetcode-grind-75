# Created by matthewkight at 7/28/23
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dir_map = [set() for i in range(numCourses)]
        for course, pre_req in prerequisites:
            dir_map[course].add(pre_req)

        # Get all those with no pre_reqs
        q = [course for course, pre_reqs in enumerate(dir_map) if len(pre_reqs) == 0]
        visited= 0
        while len(q) != 0:
            x = q.pop()
            visited += 1
            for course, pre_req in enumerate(dir_map):
                if x in pre_req:
                    dir_map[course].remove(x)
                    if len(dir_map[course]) == 0:
                        q.append(course)
        return visited == numCourses

if __name__ == '__main__':
    s = Solution()
    p = [1,4],[2,4],[3,1],[3,2]
    print(s.canFinish(numCourses=5, prerequisites=p))
