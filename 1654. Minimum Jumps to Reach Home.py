from typing import List
import collections

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        CAN_BACK,CANNOT_BACK = 1,0

        forbiddenSet = set()
        finalPos = max(x, max(forbidden)) + a + b

        print(finalPos)

        for pos in forbidden:
            forbiddenSet.add((pos,CAN_BACK))
            forbiddenSet.add((pos,CANNOT_BACK))

        q = collections.deque()
        q.append((0,CAN_BACK,0))

        while q:
            cur,backStatus,pathCount = q.popleft()

            if cur == x:
                return pathCount

            pathCount += 1

            if backStatus == CAN_BACK and cur - b > 0 and (cur-b,CANNOT_BACK) not in forbiddenSet:
                forbiddenSet.add((cur-b,CANNOT_BACK))
                q.append((cur-b,CANNOT_BACK,pathCount))

            if (cur+a,CANNOT_BACK) not in forbiddenSet and cur+a <= finalPos:
                forbiddenSet.add((cur+a,CAN_BACK))
                q.append((cur+a,CAN_BACK,pathCount))

        return -1
