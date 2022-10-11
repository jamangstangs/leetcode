import heapq
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # 상승이 2번 겹치고, 뒤에 나오는 상승이 이전에 나온 상승 범위의 위로 겹쳐야함
        # 상승 flag, 하락장 나오면 false, 상승장 나오면 true, 상승장 나온 상태에서 true이면 정답
        # 겹치는 상승장이 아니면, 최소 상승장으로 increase 변경한다. 
        flag = False
        increase = [2**31, -(2**31)-1]
        for i in range(1,len(nums)):
            if flag == False:
                if nums[i-1] < nums[i]:
                    # max 범위보다 현재 max가 더 크면, min 범위보다 현재 min이 더 크면
                    if increase[1] < nums[i] and increase[1] != -(2**31)-1:
                        return True
                    elif increase[0] < nums[i-1] and increase[0] != 2**31:
                        return True
                    else:
                        if increase[0] < nums[i] or increase[1] > nums[i-1]:
                            increase[0] = nums[i-1]
                            increase[1] = nums[i]
                            flag=True
                        else:
                            increase[0] = min(increase[0], nums[i-1])
                            increase[1] = max(increase[1], nums[i])
                            flag = True
            else:
                if nums[i-1] < nums[i]:
                    return True
                elif nums[i] > increase[0] and nums[i] < increase[1]:
                    increase[1] = nums[i]
                else:
                    flag = False
        return False

            
        