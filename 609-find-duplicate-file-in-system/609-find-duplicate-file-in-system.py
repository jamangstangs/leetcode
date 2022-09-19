from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = []
        dic = defaultdict(list)
        
        for path in paths:
            a = path.split(" ")
            d = a[0]
            for i in range(1, len(a)):
                aa = a[i].split("(")
                dic[aa[1].rstrip(")")].append(d+"/"+aa[0])
                
        for k,v in dic.items():
            if len(v) != 1:
                ans.append(v)
        return ans