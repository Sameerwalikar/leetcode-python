# 💎 Jewels and Stones

## 🧠 The Story Behind the Problem

Imagine you own a treasure chest full of stones 🪨.  
Some of them are precious jewels 💎 — and some are just ordinary rocks.

You’re given:

- `jewels` → A string representing types of stones that are **precious jewels**
- `stones` → A string representing stones you currently have

Your mission?

👉 Count how many stones in your collection are actually jewels.

⚠️ Important: Letters are **case-sensitive**.  
That means `"a"` and `"A"` are completely different stones.

---

## 📝 Examples

| Input | Output |
|-------|--------|
| jewels = `"aA"`, stones = `"aAAbbbb"` | `3` |
| jewels = `"z"`, stones = `"ZZ"` | `0` |

---

## 🔍 Understanding the Logic

We simply:

1. Go through each stone in `stones`
2. Check if that stone exists inside `jewels`
3. If yes → increase our jewel counter
4. Return the final count

It’s like checking every stone under a microscope and asking:

> “Are you precious… or just ordinary?” 💎

---

## 🚀 Approach: Direct Membership Checking

### 💡 Idea

- Loop through every character in `stones`
- If it exists in `jewels`, increase count
- Return total count

This works because string membership checking (`in`) lets us quickly verify if a stone type is a jewel.

---

## ⏱ Time Complexity

`O(n * m)`  

Where:
- `n` = length of `stones`
- `m` = length of `jewels`

(For each stone, we may scan jewels)

---

## 💾 Space Complexity

`O(1)`  

We only use a counter variable — no extra data structures.

---

## 🧑‍💻 Code

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count
```

---

## ✨ Why This Solution is Clean

- Simple
- Easy to read
- No unnecessary data structures
- Perfect for understanding string membership

---

## 🔥 Bonus Thought (For Curious Minds)

If we convert `jewels` into a set first, we can reduce lookup time and make it even more efficient.

But this version keeps the logic beautifully simple and readable.

---

## 📌 Final Takeaway

Sometimes the most powerful solutions aren’t complicated.

They’re just clear thinking + clean logic.

Keep building. Keep polishing.  
Just like jewels 💎