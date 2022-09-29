class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-1
        # 양옆에서 줄여준다. r-l = k 될때까지
        while r-l >= k:
            ll = abs(arr[l]-x)
            rr = abs(arr[r]-x)
            if ll  < rr or (ll == rr and arr[l] < arr[r]):
                r-=1
            else:
                l+=1
        
        return arr[l:r+1]
        
        
        