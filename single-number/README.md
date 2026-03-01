# 🧩 Single Number

## Problem Description

Given a **non-empty array of integers `nums`**, every element appears **twice except for one**.  
Find that single element.

You must implement a solution with:

- **Linear time complexity** → `O(n)`
- **Constant extra space** → `O(1)`

---

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- Every element appears twice except for one element.

---

## Approach 1: Using Dictionary (Hash Map)

### Idea
- Count the frequency of each number.
- Return the number whose frequency is `1`.

### Time Complexity
`O(n)`

### Space Complexity
`O(n)`

### Code

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        for key,value in dic.items():
            if(value==1):
                return key

```

---

## Approach 2: Using Set

### Idea
- If the number is not in the set, add it.
- If it already exists, remove it.
- At the end, only the single element remains in the set.

### Time Complexity
`O(n)`

### Space Complexity
`O(n)`

### Code

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=set()
        for i in nums:
            if i in res:
                res.remove(i)
            else:
                res.add(i)
        return res.pop()


        
```