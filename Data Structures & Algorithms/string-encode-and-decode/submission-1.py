class Solution:

    def encode(self, strs: List[str]) -> str:
        ab = ""
        for st in strs:
            ab = ab + st + "$XW"
        return ab


    def decode(self, s: str) -> List[str]:
        ab = s.split("$XW")
        ab.pop()
        return ab
