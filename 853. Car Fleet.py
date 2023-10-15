class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = collections.deque()
        cars = []

        for index in range(len(position)): cars.append([position[index],speed[index]])
        
        cars.sort()
        
        for index in range(len(cars)-1,-1,-1):
            stack.append((target-cars[index][0]) / cars[index][1])

            if len(stack) >= 2 and stack[-1] <= stack[-2]: stack.pop()
        
        return len(stack)