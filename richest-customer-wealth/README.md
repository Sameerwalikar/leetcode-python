# 💰 Richest Customer Wealth

> *A simple problem that teaches how to work with 2D arrays and aggregation in Python.*

## 🧠 Problem Statement

You are given an **m × n grid** `accounts`.

* `accounts[i][j]` represents the money the **iᵗʰ customer** has in the **jᵗʰ bank**.
* A customer's **wealth** = sum of all their bank accounts.

Your task is to **return the wealth of the richest customer**.

---

## 📌 Example

### Example 1

```
Input:  accounts = [[1,2,3],[3,2,1]]
Output: 6
```

**Explanation**

| Customer | Accounts  | Wealth |
| -------- | --------- | ------ |
| 1        | 1 + 2 + 3 | 6      |
| 2        | 3 + 2 + 1 | 6      |

Both customers have the same wealth, so the answer is **6**.

---

### Example 2

```
Input:  accounts = [[1,5],[7,3],[3,5]]
Output: 10
```

| Customer | Wealth |
| -------- | ------ |
| 1        | 6      |
| 2        | 10     |
| 3        | 8      |

💡 **Customer 2 is the richest.**

---

## 🚀 Approach

The idea is simple:

1. Each row represents **one customer**.
2. Calculate the **sum of each row**.
3. Track the **maximum wealth found so far**.

---

## 💻 Python Solution

```python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        
        for i in accounts:
            total = sum(i)
            maximum = max(maximum, total)
            
        return maximum
```

---

## ⚡ Pythonic One-Liner

```python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(i) for i in accounts)
```

---

## ⏱️ Complexity Analysis

| Type             | Complexity   |
| ---------------- | ------------ |
| Time Complexity  | **O(m × n)** |
| Space Complexity | **O(1)**     |

We iterate through all elements once to compute sums.

---

## 🎯 Key Concepts Practiced

* 2D Arrays
* Iteration
* Aggregation using `sum()`
* Tracking maximum values

---

## 🏁 Final Thought

Sometimes the richest customer isn't the one with the most accounts,
it's the one whose **accounts add up the most** 💸.

Happy Coding! 🚀
