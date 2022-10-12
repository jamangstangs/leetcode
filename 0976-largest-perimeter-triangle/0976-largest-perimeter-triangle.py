import heapq
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        tri = []
        maxheap = []
        for i in range(len(nums)):
            heapq.heappush(maxheap, -nums[i])
        for i in range(len(maxheap)):
            a = heapq.heappop(maxheap)
            tri.append(a)
            print(tri)
            if len(tri) == 3:
                if -tri[0] < -tri[1] - tri[2]:
                    return -(tri[0] + tri[1] + tri[2])
                else:
                    tri.pop(0)
        return 0
                