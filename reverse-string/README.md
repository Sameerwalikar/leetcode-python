# 🔁 Reverse String

## 🧠 Problem Description

Write a function that reverses a string.

The input string is given as an array of characters `s`.

⚠️ You must modify the input array **in-place** with `O(1)` extra memory.

---

## 📝 Example

| Input | Output |
|--------|--------|
| `["h","e","l","l","o"]` | `["o","l","l","e","h"]` |
| `["H","a","n","n","a","h"]` | `["h","a","n","n","a","H"]` |

---

## 🎯 Key Requirement

- Do **not** return anything.
- Modify the list directly.
- Use only constant extra space.

---

# 🚀 Approach: Two Pointer Technique

## 💡 The Core Idea

Imagine the string as a rope.

We grab:
- One end with the **left pointer**
- One end with the **right pointer**

Then we:

1. Swap both characters
2. Move both pointers inward
3. Repeat until they meet

This way, we reverse the string **in-place**, without using extra memory.

---

## 🔍 Step-by-Step Visualization

For: `["h","e","l","l","o"]`

Step 1: swap `h` and `o`  
Step 2: swap `e` and `l`  
Middle element stays same  

Final: `["o","l","l","e","h"]`

---

## ⏱ Time Complexity

`O(n)`  

We traverse the string once (half actually).

---

## 💾 Space Complexity

`O(1)`  

No extra data structures used.  
Only two pointer variables.

---

## 🧑‍💻 Code

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = 0
        r = len(s) - 1
        
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
```

---

## ✨ Why This is a Strong Solution

- Uses classic **two-pointer technique**
- In-place modification
- No extra memory
- Clean and interview-friendly

---

## 🏆 DSA Pattern Learned

👉 Two Pointers  

This pattern appears in:
- Reversing arrays
- Palindrome problems
- Sorting problems
- Sliding window techniques

Master this pattern, and you unlock many array/string problems 🔓