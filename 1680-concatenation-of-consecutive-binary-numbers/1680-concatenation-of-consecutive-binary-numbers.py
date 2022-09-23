class Solution:
    def concatenatedBinary(self, n: int) -> int:
        bi = "0b"
        for i in range(1, n+1):
            bi += bin(i).lstrip("0b")
        return int(bi,2) % 1000000007
            