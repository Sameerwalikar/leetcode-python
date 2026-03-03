# 🔢 Sqrt(x)

## 🧠 Problem Description

Given a non-negative integer `x`, compute and return the square root of `x`.

Since the return type is an integer, the decimal part is truncated.

You must not use any built-in exponent function or operator.

---

## 📝 Examples

| Input | Output |
|--------|--------|
| `x = 4` | `2` |
| `x = 8` | `2` |

Explanation:  
The square root of 8 is 2.82842…, and since we truncate the decimal part, the result is 2.

---

# 🚀 Approach 1: Normal Iterative Method

## 💡 Idea

- Start from `1`
- Keep increasing the number
- Stop when `number²` becomes greater than `x`
- Return the previous number

This works but is not efficient for large values.

---

## ⏱ Time Complexity

`O(√x)`

---

## 💾 Space Complexity

`O(1)`

---

## 🧑‍💻 Code

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        number = 1
        while number * number <= x:
            number += 1
        return number - 1
```

---

# 🚀 Approach 2: Binary Search (Optimized)

## 💡 Why Binary Search?

The square root lies between `1` and `x`.

Instead of checking every number, we:
- Pick the middle value
- Compare `mid²` with `x`
- Eliminate half of the search space

This makes it significantly faster.

---

## 🔍 Core Logic

- If `mid² == x` → return `mid`
- If `mid² > x` → search left half
- If `mid² < x` → search right half
- If not exact → return `right` (floor value)

---

## ⏱ Time Complexity

`O(log x)`

---

## 💾 Space Complexity

`O(1)`

---

## 🧑‍💻 Code

```python
class Solution:
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
```

---

# 🏆 Pattern Learned

👉 Binary Search on Answer Space  

This pattern is extremely powerful and appears in:
- Square root problems
- Finding minimum feasible value
- Peak element problems
- Allocation problems

---

## ✨ Final Takeaway

Normal method = Simple but slow  
Binary Search = Smart and scalable  

This is the difference between brute force thinking and algorithmic thinking.