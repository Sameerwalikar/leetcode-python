# 🧩 Fizz Buzz

## Problem Description

Given an integer `n`, return a string array `answer` (1-indexed) where:

- `answer[i] == "FizzBuzz"` if `i` is divisible by 3 and 5.
- `answer[i] == "Fizz"` if `i` is divisible by 3.
- `answer[i] == "Buzz"` if `i` is divisible by 5.
- `answer[i] == i` (as a string) if none of the above conditions are true.

---

## Examples

| Input | Output |
|-------|--------|
| `n = 3` | `["1","2","Fizz"]` |
| `n = 5` | `["1","2","Fizz","4","Buzz"]` |
| `n = 15` | `["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]` |

---

## Constraints

- `1 <= n <= 10^4`

---

## Approach: Conditional Checking

### Idea
- Iterate from `1` to `n`.
- If number divisible by both `3` and `5`, append `"FizzBuzz"`.
- Else if divisible by `3`, append `"Fizz"`.
- Else if divisible by `5`, append `"Buzz"`.
- Otherwise, append the number as a string.

### Time Complexity
`O(n)`

### Space Complexity
`O(n)` (result array)

### Code

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            if (i % 3 == 0 and i % 5 == 0):
                answer.append("FizzBuzz")
            elif (i % 3 == 0):
                answer.append("Fizz")
            elif (i % 5 == 0):
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer
```