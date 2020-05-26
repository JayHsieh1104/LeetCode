class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[-1 * i - 1] = s[-1 * i - 1], s[i]
        return s        