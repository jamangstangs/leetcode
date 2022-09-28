class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        l, ptr = 0, head
        
        while ptr:
            ptr = ptr.next
            l+=1
        
        # 맨 앞에 빼준다. 
        if l == n:
            return head.next
        
        # n번째 이전까지 가야한다. 
        ptr = head
        l -= n+1
        while l>0:
            ptr = ptr.next
            l-=1
        ptr.next = ptr.next.next
        return head
