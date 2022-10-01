import copy
class Solution:
    def numDecodings(self, s: str) -> int:
        d = [0]*101
        d[0] = 1
        if s[0] == "0":
            d[1] = 0
        else:
            d[1] = 1
        
        # d[i] = d[i-1] + d[i-2]
        for i in range(2, len(s)+1):
            n = s[i-1:i]
            nn = s[i-2:i]
            if int(n) >= 1:
                d[i] += d[i-1]
            if int(nn) >= 10 and int(nn)<=26:
                d[i] += d[i-2]
        return d[len(s)]
                    
                
                
                
                