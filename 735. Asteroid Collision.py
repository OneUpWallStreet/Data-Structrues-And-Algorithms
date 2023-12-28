class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = collections.deque()

        for ch in asteroids:

            while stack and ch < 0 and stack[-1] > 0:
                
                diff = stack[-1] + ch

                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    ch = 0
                elif diff == 0:
                    ch = 0
                    stack.pop()
            if ch != 0: stack.append(ch)

        return list(stack)