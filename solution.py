class Solution:

    def run(self, s: str) -> int:
        charSet = set()
        counter = 0
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            counter = max(counter, r - l + 1)
        return counter
