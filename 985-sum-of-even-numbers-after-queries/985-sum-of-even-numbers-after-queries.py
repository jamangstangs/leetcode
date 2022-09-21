class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        esum = 0
        for i in nums:
            if i % 2 == 0:
                esum += i
        ans = []

        # esum 초기에 넣고, 
        for i in queries:
            oval = nums[i[1]]
            nums[i[1]] = nums[i[1]] + i[0]
            if nums[i[1]] % 2 == 0:
                if oval % 2 == 0:
                    esum += i[0]
                else:
                    esum += nums[i[1]]
            else:
                if oval % 2 ==0:
                    esum -= oval
            ans.append(esum)
        return ans
            
        
# 홀수 -> 짝수
# 홀수 -> 홀수
# 짝수 -> 짝수
# 짝수 -> 홀수