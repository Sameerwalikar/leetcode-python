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