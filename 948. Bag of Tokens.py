class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        tokens.sort()
        result = 0
        l, r = 0, len(tokens) - 1

        while l <= r:
            if power - tokens[l] >= 0: 
                result += 1
                power -= tokens[l]
                l += 1
            elif result >= 1 and r != l:
                power += tokens[r]
                result -= 1
                r -= 1
            else: break

        return result    