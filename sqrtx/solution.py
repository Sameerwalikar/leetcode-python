class Solution:
    # Normal Math Approach
    def mySqrt(self, x: int) -> int:
        number = 1
        while number * number <= x:
            number += 1
        return number - 1


class Solution:
    # Binary Search Approach (Optimized)
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1

        return right