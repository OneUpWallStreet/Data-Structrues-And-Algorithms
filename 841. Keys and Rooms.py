from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set()
        def dfs(key: int):
            keys.add(key)
            for unlockedKey in rooms[key]:
                # Ignore keys we already collected
                # somewhere else
                if unlockedKey not in keys:
                    dfs(unlockedKey)
        dfs(0)
        return len(keys) == len(rooms)