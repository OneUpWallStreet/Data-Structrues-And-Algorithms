class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = first = 0
        for row in bank:
            if row.count("1") == 0: continue
            if first == 0: first = row.count("1")
            else:
                result += first * row.count("1")
                first = row.count("1")
        return result