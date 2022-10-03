class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        index = []
        flag = False
        front = 0
        ans = 0
        c = colors+"."
        for i in range(1, len(c)):
            if c[front] == c[i] and flag == False:
                flag = True
                continue
            elif c[front] != c[i] and flag == True:
                index.append((front, i-1))
                front = i
                flag = False
            elif c[front] != c[i] and flag == False:
                front +=1
                
        for i,j in index:
            # 최대 하나 남기고 다 터뜨리자
            m = 0
            t = 0
            for k in range(i, j+1):
                m = max(m, neededTime[k])
                t += neededTime[k]
            ans += t-m
        return ans
                
                
                
            
            