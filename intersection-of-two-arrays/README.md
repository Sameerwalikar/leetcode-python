# 🧩 Intersection of Two Arrays

## Problem Description

Given two integer arrays `nums1` and `nums2`, return an array of their intersection.

- Each element in the result must be **unique**.
- You may return the result in **any order**.

---

## Examples

| Input | Output |
|-------|--------|
| `nums1 = [1,2,2,1], nums2 = [2,2]` | `[2]` |
| `nums1 = [4,9,5], nums2 = [9,4,9,8,4]` | `[9,4]` |

Explanation: `[4,9]` is also accepted.

---

## Constraints

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`

---

## Approach 1: Brute Force with Duplicate Check

### Idea
- Iterate through each element in `nums1`.
- Check if it exists in `nums2`.
- If it exists and is not already in the result list, add it.
- This ensures uniqueness in the final answer.

### Time Complexity
`O(n * m)`

### Space Complexity
`O(k)`  
(where `k` is the number of unique intersecting elements)

### Code

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list1 = []
        for i in nums1:
            if i in nums2:
                if i not in list1:
                    list1.append(i)
        return list1
```

---

## Approach 2: Using Sets (Optimized)

### Idea
- Store all elements of `nums1` in a set.
- Iterate through `nums2`.
- If element exists in the set, add it to answer set.
- Convert final set to list.

Using sets gives **constant time membership checking**, improving performance.

### Time Complexity
`O(n + m)`

### Space Complexity
`O(n + k)`

### Code

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set()
        ans = set()

        for i in nums1:
            s.add(i)

        for j in nums2:
            if j in s:
                ans.add(j)

        return list(ans)
```