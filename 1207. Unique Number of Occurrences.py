class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        hashtable = defaultdict(int)
        hashset = set()

        for num in arr:
            hashtable[num] += 1

        for value in hashtable.values():
            if value in hashset:
                return False
            else:
                hashset.add(value)

        return True