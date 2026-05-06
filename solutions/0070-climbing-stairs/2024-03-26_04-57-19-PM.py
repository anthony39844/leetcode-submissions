class Solution:
    def climbStairs(self, n: int) -> int:
        answers = {}
        def fib(n):
            if n == 0:
                return 1
            elif n == 1:
                return 1

            # Check if the value has already been computed
            if n in answers:
                return answers[n]

            # Compute Fibonacci recursively and store the result
            answers[n] = fib(n - 1) + fib(n - 2)
            return answers[n]

        return fib(n)



