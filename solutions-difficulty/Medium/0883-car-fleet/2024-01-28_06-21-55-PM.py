class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        
        stack = []
        pairs = []
        for i in range(len(position)):
            pairs.append([position[i], speed[i]])
        for i in sorted(pairs)[::-1]:
            if not stack:
                stack.append(i)
            else:
                curr_time = (target - i[0]) / i[1]
                time = (target - stack[-1][0]) / stack[-1][1]

                if curr_time > time: #if the time for the current car is greater than the car in the stack
                                     #that means it wont become a fleet so we append the car to the stack
                    stack.append(i)


        return len(stack)
