class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for a in nums:
            if a in duplicate.keys():
                duplicate[a] = duplicate.get(a,0) + 1
            else:
                duplicate[a] = 1

        dup = False

        for key, value in duplicate.items():
            if value > 1:
                dup = True
                break

        return dup

        