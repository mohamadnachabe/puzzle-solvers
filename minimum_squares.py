class Solver:
    def __init__(self):
        self.memo = {}

    def minimum_squares(self, target_sum):
        def helper(n):
            if n in self.memo:
                return self.memo[n]

            if n == 0:
                return 0

            minimum = n

            for i in range(1, n + 1):
                if i ** 2 > n:
                    break
                self.memo[n] = min(1 + helper(n - i ** 2), minimum)

            return self.memo[n]

        r = helper(target_sum)
        return r


if __name__ == '__main__':
    print(Solver().minimum_squares(60))