class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        for i in s.split():
            ans = ans + i[::-1] + " "
        return ans.rstrip(" ")