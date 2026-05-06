class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        
        stack = []
        pairs = []

        for i in range(len(position)): #we are making a list of tuples of the position and speed for each car
            pairs.append([position[i], speed[i]])

        for i in sorted(pairs)[::-1]: #loop through that list backwards
            if not stack: 
                stack.append(i)
            else:
                curr_time = (target - i[0]) / i[1]
                time = (target - stack[-1][0]) / stack[-1][1]

                if curr_time > time: #if the time for the current car is greater than the car in the stack
                                     #that means it wont become a fleet so we append the car to the stack
                    stack.append(i)
        # the idea is that we will use how long it takes for each car to reach the target by dividing the 
        # distance it is away from the target by its speed. If the time it needs is greater than the car closest
        # to the target, then it will become its own fleet of cars. If it is less than, then it will join the
        # a fleet so we dont append that car to the stack. The length of the stack at the end is the number of fleets

        return len(stack)
