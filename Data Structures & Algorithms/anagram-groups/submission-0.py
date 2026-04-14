from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for a in strs:
            key = ''.join(sorted(a))
            output[key].append(a)

        return output.values()