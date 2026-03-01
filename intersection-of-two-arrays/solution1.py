class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list1 = []
        for i in nums1:
            if i in nums2:
                if i not in list1:
                    list1.append(i)
        return list1